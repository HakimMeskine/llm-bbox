# ESP32 Button Box - RGB LED Control
# This file contains functions for controlling the WS2812B RGB LEDs

import time
import machine
import neopixel
import socket
import json
import _thread
from machine import Pin
import config

# Initialize the NeoPixel strip
np = None
led_lock = _thread.allocate_lock()  # Thread lock for LED access
simhub_thread = None
simhub_socket = None
current_effect = config.LED_EFFECTS["STATIC"]
current_colors = [config.DEFAULT_COLORS["OFF"]] * config.RGB_LED_COUNT
button_press_time = [0] * config.RGB_LED_COUNT

def init():
    """Initialize the RGB LED strip"""
    global np
    
    if not config.RGB_LED_ENABLED:
        print("RGB LEDs disabled in config")
        return False
    
    try:
        # Initialize the NeoPixel strip
        led_pin = Pin(config.RGB_LED_PIN, Pin.OUT)
        np = neopixel.NeoPixel(led_pin, config.RGB_LED_COUNT)
        
        # Set all LEDs to off
        clear()
        
        print(f"RGB LEDs initialized: {config.RGB_LED_COUNT} LEDs on pin {config.RGB_LED_PIN}")
        
        # Start SimHub communication thread if enabled
        if config.SIMHUB_ENABLED and config.WIFI_ENABLED:
            start_simhub_thread()
        
        return True
    except Exception as e:
        print(f"Error initializing RGB LEDs: {e}")
        return False

def clear():
    """Turn off all LEDs"""
    if np is None or not config.RGB_LED_ENABLED:
        return
    
    with led_lock:
        for i in range(config.RGB_LED_COUNT):
            np[i] = (0, 0, 0)
        np.write()

def set_brightness(brightness):
    """Set the brightness of all LEDs (0-255)"""
    if brightness < 0:
        brightness = 0
    elif brightness > 255:
        brightness = 255
    
    config.RGB_LED_BRIGHTNESS = brightness

def set_color(led_index, color, write=True):
    """Set the color of a specific LED"""
    if np is None or not config.RGB_LED_ENABLED:
        return
    
    if led_index < 0 or led_index >= config.RGB_LED_COUNT:
        return
    
    # Apply brightness
    r = int(color[0] * config.RGB_LED_BRIGHTNESS / 255)
    g = int(color[1] * config.RGB_LED_BRIGHTNESS / 255)
    b = int(color[2] * config.RGB_LED_BRIGHTNESS / 255)
    
    with led_lock:
        np[led_index] = (r, g, b)
        current_colors[led_index] = color
        if write:
            np.write()

def set_all_colors(color, write=True):
    """Set all LEDs to the same color"""
    if np is None or not config.RGB_LED_ENABLED:
        return
    
    with led_lock:
        for i in range(config.RGB_LED_COUNT):
            set_color(i, color, False)
        if write:
            np.write()

def set_button_color(button_num, color, write=True):
    """Set the color of the LED for a specific button"""
    if button_num not in config.BUTTON_LED_MAP:
        return
    
    led_index = config.BUTTON_LED_MAP[button_num]
    set_color(led_index, color, write)

def button_pressed(button_num):
    """Handle button press event for reactive lighting"""
    if current_effect != config.LED_EFFECTS["REACTIVE"] or button_num not in config.BUTTON_LED_MAP:
        return
    
    led_index = config.BUTTON_LED_MAP[button_num]
    button_press_time[led_index] = time.ticks_ms()
    set_color(led_index, config.DEFAULT_COLORS["WHITE"])

def update_effects():
    """Update LED effects based on the current effect mode"""
    if np is None or not config.RGB_LED_ENABLED:
        return
    
    if current_effect == config.LED_EFFECTS["STATIC"]:
        # Static effect - nothing to update
        pass
    
    elif current_effect == config.LED_EFFECTS["BREATHING"]:
        # Breathing effect - fade in and out
        breathing_update()
    
    elif current_effect == config.LED_EFFECTS["RAINBOW"]:
        # Rainbow effect - cycle through colors
        rainbow_update()
    
    elif current_effect == config.LED_EFFECTS["REACTIVE"]:
        # Reactive effect - fade out after button press
        reactive_update()
    
    elif current_effect == config.LED_EFFECTS["SIMHUB"]:
        # SimHub effect - controlled by SimHub
        # Nothing to do here, SimHub thread handles updates
        pass

def breathing_update():
    """Update breathing effect"""
    if np is None:
        return
    
    # Calculate brightness based on time
    t = time.ticks_ms() / 1000  # Time in seconds
    # Sine wave oscillation between 0 and 1
    brightness = (math.sin(t * 2) + 1) / 2
    
    with led_lock:
        for i in range(config.RGB_LED_COUNT):
            color = current_colors[i]
            r = int(color[0] * brightness)
            g = int(color[1] * brightness)
            b = int(color[2] * brightness)
            np[i] = (r, g, b)
        np.write()

def rainbow_update():
    """Update rainbow effect"""
    if np is None:
        return
    
    # Calculate hue based on time
    t = time.ticks_ms() / 10  # Time in 10ms increments
    
    with led_lock:
        for i in range(config.RGB_LED_COUNT):
            # Each LED gets a slightly different hue
            hue = (t + i * 10) % 360
            r, g, b = hsv_to_rgb(hue, 1.0, 1.0)
            np[i] = (r, g, b)
        np.write()

def reactive_update():
    """Update reactive effect"""
    if np is None:
        return
    
    current_time = time.ticks_ms()
    update_needed = False
    
    with led_lock:
        for i in range(config.RGB_LED_COUNT):
            if button_press_time[i] > 0:
                # Calculate time since button press
                elapsed = time.ticks_diff(current_time, button_press_time[i])
                
                if elapsed > 500:  # Fade out after 500ms
                    np[i] = (0, 0, 0)
                    button_press_time[i] = 0
                    update_needed = True
                elif elapsed > 200:  # Start fading out after 200ms
                    fade_factor = 1.0 - (elapsed - 200) / 300
                    r = int(255 * fade_factor)
                    g = int(255 * fade_factor)
                    b = int(255 * fade_factor)
                    np[i] = (r, g, b)
                    update_needed = True
        
        if update_needed:
            np.write()

def hsv_to_rgb(h, s, v):
    """Convert HSV color to RGB
    
    Args:
        h: Hue (0-360)
        s: Saturation (0-1)
        v: Value (0-1)
        
    Returns:
        tuple: (r, g, b) values (0-255)
    """
    if s == 0.0:
        return (int(v * 255), int(v * 255), int(v * 255))
    
    h /= 60
    i = int(h)
    f = h - i
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))
    
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q
    
    return (int(r * 255), int(g * 255), int(b * 255))

def set_effect(effect):
    """Set the current LED effect"""
    global current_effect
    
    if effect not in config.LED_EFFECTS.values():
        return
    
    current_effect = effect
    
    # Initialize effect
    if effect == config.LED_EFFECTS["STATIC"]:
        # Do nothing, keep current colors
        pass
    
    elif effect == config.LED_EFFECTS["BREATHING"]:
        # Start with current colors
        pass
    
    elif effect == config.LED_EFFECTS["RAINBOW"]:
        # Start with rainbow colors
        pass
    
    elif effect == config.LED_EFFECTS["REACTIVE"]:
        # Start with all LEDs off
        clear()
    
    elif effect == config.LED_EFFECTS["SIMHUB"]:
        # Start with all LEDs off
        clear()

def start_simhub_thread():
    """Start the SimHub communication thread"""
    global simhub_thread
    
    if not config.SIMHUB_ENABLED or not config.WIFI_ENABLED:
        return
    
    # Start the thread
    simhub_thread = _thread.start_new_thread(simhub_listener, ())

def simhub_listener():
    """Thread function for listening to SimHub UDP messages"""
    global simhub_socket
    
    try:
        # Create UDP socket
        simhub_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        simhub_socket.bind(('0.0.0.0', config.SIMHUB_PORT))
        
        print(f"SimHub listener started on port {config.SIMHUB_PORT}")
        
        while True:
            try:
                # Receive data
                data, addr = simhub_socket.recvfrom(1024)
                
                # Parse JSON data
                try:
                    message = json.loads(data.decode('utf-8'))
                    process_simhub_message(message)
                except ValueError:
                    print("Invalid JSON data received from SimHub")
            
            except Exception as e:
                print(f"Error in SimHub listener: {e}")
                time.sleep(1)
    
    except Exception as e:
        print(f"Failed to start SimHub listener: {e}")

def process_simhub_message(message):
    """Process a message from SimHub"""
    if 'type' not in message:
        return
    
    if message['type'] == 'led':
        # LED control message
        if 'leds' in message:
            with led_lock:
                for led_data in message['leds']:
                    if 'id' in led_data and 'color' in led_data:
                        led_id = led_data['id']
                        color = led_data['color']
                        
                        if led_id < 0 or led_id >= config.RGB_LED_COUNT:
                            continue
                        
                        if isinstance(color, str) and color.startswith('#'):
                            # Convert hex color to RGB
                            r = int(color[1:3], 16)
                            g = int(color[3:5], 16)
                            b = int(color[5:7], 16)
                            set_color(led_id, (r, g, b), False)
                        elif isinstance(color, list) and len(color) >= 3:
                            # RGB color
                            set_color(led_id, (color[0], color[1], color[2]), False)
                
                np.write()
    
    elif message['type'] == 'effect':
        # Effect control message
        if 'effect' in message:
            effect_name = message['effect']
            if effect_name in config.LED_EFFECTS:
                set_effect(config.LED_EFFECTS[effect_name])
    
    elif message['type'] == 'brightness':
        # Brightness control message
        if 'value' in message:
            set_brightness(message['value'])
