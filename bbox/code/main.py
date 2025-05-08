# ESP32 Button Box - Main Application
# This is the main entry point for the button box firmware

import time
import machine
import config
import button_matrix
import rotary_encoders
import funky_switch
import usb_hid

# Status LEDs
status_led1 = None
status_led2 = None

# Mapping of inputs to HID buttons/axes
# Button matrix: Buttons 1-20 map to HID buttons 1-20
# Rotary encoder buttons: Map to HID buttons 21-22
# Funky switch button: Maps to HID button 23
# Funky switch directions: Map to HID buttons 24-31
# Rotary encoders: Map to HID axes 1-2

def init_status_leds():
    """Initialize the status LEDs"""
    global status_led1, status_led2
    
    status_led1 = machine.Pin(config.STATUS_LED1_PIN, machine.Pin.OUT)
    status_led2 = machine.Pin(config.STATUS_LED2_PIN, machine.Pin.OUT)
    
    # Initial LED state
    status_led1.value(1)  # Turn on LED 1
    status_led2.value(0)  # Turn off LED 2

def blink_status_led(led, count=1, on_time=100, off_time=100):
    """Blink a status LED"""
    for _ in range(count):
        led.value(1)
        time.sleep_ms(on_time)
        led.value(0)
        time.sleep_ms(off_time)

def init_all_modules():
    """Initialize all modules"""
    print("Initializing button box...")
    
    # Initialize modules
    button_matrix.init()
    print("Button matrix initialized")
    
    rotary_encoders.init()
    print("Rotary encoders initialized")
    
    funky_switch.init()
    print("Funky switch initialized")
    
    usb_hid_success = usb_hid.init()
    if usb_hid_success:
        print("USB HID initialized")
    else:
        print("USB HID initialization failed or disabled")
    
    # Reset all HID states
    usb_hid.reset_all()
    
    print("All modules initialized")
    return True

def process_button_matrix():
    """Process button matrix inputs"""
    # Scan the button matrix
    pressed_buttons = button_matrix.scan()
    
    # Process newly pressed buttons
    for button_num in pressed_buttons:
        print(f"Button {button_num} pressed")
        
        # Map button to HID button
        usb_hid.set_button(button_num, True)
        
        # Blink status LED for visual feedback
        blink_status_led(status_led2, 1, 50, 0)

def process_rotary_encoders():
    """Process rotary encoder inputs"""
    # Check encoder 1
    encoder1_change = rotary_encoders.read_encoder1()
    if encoder1_change != 0:
        print(f"Encoder 1 change: {encoder1_change}")
        
        # Map encoder to HID axis
        # Scale to 0-255 range with center at 128
        current_value = usb_hid.axis_states[0]
        new_value = max(0, min(255, current_value + encoder1_change * 8))
        usb_hid.set_axis(1, new_value)
        
        # Gradually return to center
        time.sleep_ms(50)
        usb_hid.set_axis(1, 128)
    
    # Check encoder 2
    encoder2_change = rotary_encoders.read_encoder2()
    if encoder2_change != 0:
        print(f"Encoder 2 change: {encoder2_change}")
        
        # Map encoder to HID axis
        # Scale to 0-255 range with center at 128
        current_value = usb_hid.axis_states[1]
        new_value = max(0, min(255, current_value + encoder2_change * 8))
        usb_hid.set_axis(2, new_value)
        
        # Gradually return to center
        time.sleep_ms(50)
        usb_hid.set_axis(2, 128)
    
    # Check encoder buttons
    encoder_buttons = rotary_encoders.check_encoder_buttons()
    for button in encoder_buttons:
        if button == "ENCODER1_BUTTON":
            print("Encoder 1 button pressed")
            usb_hid.set_button(21, True)
            time.sleep_ms(50)
            usb_hid.set_button(21, False)
        elif button == "ENCODER2_BUTTON":
            print("Encoder 2 button pressed")
            usb_hid.set_button(22, True)
            time.sleep_ms(50)
            usb_hid.set_button(22, False)

def process_funky_switch():
    """Process funky switch inputs"""
    # Check direction changes
    direction = funky_switch.check_direction_change()
    if direction:
        print(f"Funky switch direction: {direction}")
        
        # Map direction to HID button
        if direction == funky_switch.DIRECTION_UP:
            usb_hid.set_button(24, True)
            time.sleep_ms(50)
            usb_hid.set_button(24, False)
        elif direction == funky_switch.DIRECTION_DOWN:
            usb_hid.set_button(25, True)
            time.sleep_ms(50)
            usb_hid.set_button(25, False)
        elif direction == funky_switch.DIRECTION_LEFT:
            usb_hid.set_button(26, True)
            time.sleep_ms(50)
            usb_hid.set_button(26, False)
        elif direction == funky_switch.DIRECTION_RIGHT:
            usb_hid.set_button(27, True)
            time.sleep_ms(50)
            usb_hid.set_button(27, False)
        elif direction == funky_switch.DIRECTION_UP_LEFT:
            usb_hid.set_button(28, True)
            time.sleep_ms(50)
            usb_hid.set_button(28, False)
        elif direction == funky_switch.DIRECTION_UP_RIGHT:
            usb_hid.set_button(29, True)
            time.sleep_ms(50)
            usb_hid.set_button(29, False)
        elif direction == funky_switch.DIRECTION_DOWN_LEFT:
            usb_hid.set_button(30, True)
            time.sleep_ms(50)
            usb_hid.set_button(30, False)
        elif direction == funky_switch.DIRECTION_DOWN_RIGHT:
            usb_hid.set_button(31, True)
            time.sleep_ms(50)
            usb_hid.set_button(31, False)
    
    # Check button press
    if funky_switch.check_button():
        print("Funky switch button pressed")
        usb_hid.set_button(23, True)
        time.sleep_ms(50)
        usb_hid.set_button(23, False)

def main_loop():
    """Main application loop"""
    print("Starting main loop...")
    
    # Turn on status LED 1 to indicate running
    status_led1.value(1)
    
    try:
        while True:
            # Process inputs
            process_button_matrix()
            process_rotary_encoders()
            process_funky_switch()
            
            # Send HID report
            usb_hid.send_report()
            
            # Small delay to prevent CPU hogging
            time.sleep_ms(config.MATRIX_SCAN_INTERVAL_MS)
            
            # Toggle status LED 1 every second for heartbeat
            if time.ticks_ms() % 1000 < 100:
                status_led1.value(not status_led1.value())
    
    except KeyboardInterrupt:
        print("Program interrupted")
    except Exception as e:
        print(f"Error in main loop: {e}")
    finally:
        # Clean up
        status_led1.value(0)
        status_led2.value(0)
        print("Program terminated")

# Main entry point
if __name__ == "__main__":
    # Initialize status LEDs
    init_status_leds()
    
    # Blink LEDs to indicate startup
    for _ in range(3):
        status_led1.value(1)
        status_led2.value(0)
        time.sleep_ms(100)
        status_led1.value(0)
        status_led2.value(1)
        time.sleep_ms(100)
    
    # Initialize all modules
    if init_all_modules():
        # Start the main loop
        main_loop()
    else:
        # Initialization failed, blink error pattern
        print("Initialization failed")
        for _ in range(10):
            status_led1.value(1)
            status_led2.value(1)
            time.sleep_ms(100)
            status_led1.value(0)
            status_led2.value(0)
            time.sleep_ms(100)
