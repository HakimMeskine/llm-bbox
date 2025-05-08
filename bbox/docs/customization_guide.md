# ESP32 Button Box - Customization Guide

This guide provides information on how to customize the ESP32 button box for different applications. The button box is designed to be flexible and can be adapted to various use cases such as gaming, media control, productivity, and more.

## Software Customization

### Button Mapping

The button mapping can be customized by modifying the `main.py` file. The default mapping is:

- Button matrix (20 buttons): HID buttons 1-20
- Rotary encoder buttons (2): HID buttons 21-22
- Funky switch button: HID button 23
- Funky switch directions (8): HID buttons 24-31
- Rotary encoders (2): HID axes 1-2

To change this mapping, modify the corresponding sections in the `process_button_matrix()`, `process_rotary_encoders()`, and `process_funky_switch()` functions in `main.py`.

Example of changing a button mapping:

```python
# Original mapping
usb_hid.set_button(button_num, True)  # Maps button 1 to HID button 1, button 2 to HID button 2, etc.

# Custom mapping (e.g., map button 1 to HID button 5)
if button_num == 1:
    usb_hid.set_button(5, True)
else:
    usb_hid.set_button(button_num, True)
```

### Button Behavior

You can customize the behavior of buttons by modifying how they're processed in `main.py`. For example:

- **Toggle buttons**: Buttons that stay pressed until pressed again
- **Macro buttons**: Buttons that trigger multiple actions
- **Shift buttons**: Buttons that change the function of other buttons when held

Example of implementing a toggle button:

```python
# Add to the top of main.py
button_toggle_states = {}  # Dictionary to track toggle states

# Modify process_button_matrix()
def process_button_matrix():
    """Process button matrix inputs with toggle functionality"""
    # Scan the button matrix
    pressed_buttons = button_matrix.scan()
    
    # Process newly pressed buttons
    for button_num in pressed_buttons:
        print(f"Button {button_num} pressed")
        
        # Toggle button state
        if button_num not in button_toggle_states:
            button_toggle_states[button_num] = False
        
        button_toggle_states[button_num] = not button_toggle_states[button_num]
        
        # Map button to HID button
        usb_hid.set_button(button_num, button_toggle_states[button_num])
        
        # Blink status LED for visual feedback
        blink_status_led(status_led2, 1, 50, 0)
```

### Rotary Encoder Behavior

The rotary encoders can be customized to control different parameters:

- **Continuous control**: Volume, scrolling, etc.
- **Stepped control**: Menu navigation, item selection, etc.
- **Acceleration**: Faster turning results in larger value changes

Example of implementing acceleration for rotary encoders:

```python
# Add to the top of main.py
last_encoder_time = 0
encoder_speed = 0

# Modify process_rotary_encoders()
def process_rotary_encoders():
    """Process rotary encoder inputs with acceleration"""
    global last_encoder_time, encoder_speed
    
    # Check encoder 1
    encoder1_change = rotary_encoders.read_encoder1()
    if encoder1_change != 0:
        # Calculate time since last change
        current_time = time.ticks_ms()
        time_diff = time.ticks_diff(current_time, last_encoder_time)
        last_encoder_time = current_time
        
        # Calculate speed (smaller time_diff = faster turning)
        if time_diff < 50:
            encoder_speed = 4  # Fast
        elif time_diff < 100:
            encoder_speed = 2  # Medium
        else:
            encoder_speed = 1  # Slow
        
        print(f"Encoder 1 change: {encoder1_change}, Speed: {encoder_speed}")
        
        # Apply acceleration
        value_change = encoder1_change * encoder_speed
        
        # Map encoder to HID axis with acceleration
        current_value = usb_hid.axis_states[0]
        new_value = max(0, min(255, current_value + value_change * 8))
        usb_hid.set_axis(1, new_value)
        
        # Gradually return to center
        time.sleep_ms(50)
        usb_hid.set_axis(1, 128)
    
    # Similar modifications for encoder 2...
```

### Funky Switch Behavior

The funky switch can be customized for different navigation patterns:

- **Directional control**: Arrow keys, camera control, etc.
- **Mode selection**: Different directions select different modes
- **Combined with buttons**: Directions + button combinations

Example of implementing mode selection with the funky switch:

```python
# Add to the top of main.py
current_mode = 0  # 0: Normal, 1: Shift, 2: Alt
mode_names = ["Normal", "Shift", "Alt"]

# Modify process_funky_switch()
def process_funky_switch():
    """Process funky switch inputs with mode selection"""
    global current_mode
    
    # Check direction changes
    direction = funky_switch.check_direction_change()
    if direction:
        print(f"Funky switch direction: {direction}")
        
        # Use Up/Down to change modes
        if direction == funky_switch.DIRECTION_UP:
            current_mode = (current_mode + 1) % len(mode_names)
            print(f"Mode changed to: {mode_names[current_mode]}")
            # Blink LED to indicate mode change
            blink_status_led(status_led1, current_mode + 1, 100, 100)
        elif direction == funky_switch.DIRECTION_DOWN:
            current_mode = (current_mode - 1) % len(mode_names)
            print(f"Mode changed to: {mode_names[current_mode]}")
            # Blink LED to indicate mode change
            blink_status_led(status_led1, current_mode + 1, 100, 100)
        # Other directions can still be mapped to buttons
        elif direction == funky_switch.DIRECTION_LEFT:
            usb_hid.set_button(26, True)
            time.sleep_ms(50)
            usb_hid.set_button(26, False)
        # ... other directions
    
    # Check button press
    if funky_switch.check_button():
        print("Funky switch button pressed")
        usb_hid.set_button(23, True)
        time.sleep_ms(50)
        usb_hid.set_button(23, False)
```

## Hardware Customization

### Alternative Button Types

You can replace the standard tactile buttons with different types:

- **Mechanical switches**: Cherry MX, Gateron, etc. for better feel
- **Arcade buttons**: For a more traditional arcade feel
- **Illuminated buttons**: For visual feedback

Note: Different button types may require adjustments to the PCB design and enclosure.

### Custom Enclosure

The enclosure can be customized to fit your specific needs:

- **3D printed**: Design your own enclosure with CAD software
- **Laser-cut acrylic**: For a more professional look
- **Wood**: For a classic, premium feel

Design considerations:
- Ensure adequate space for all components
- Include mounting points for the PCB
- Provide access to the USB port
- Consider ergonomics for comfortable use

### Additional Features

You can add extra features to the button box:

- **OLED display**: To show current mode, button functions, etc.
- **Additional inputs**: More buttons, joysticks, etc.
- **Wireless connectivity**: Bluetooth or WiFi for wireless operation

## RGB LED Customization

The button box includes WS2812B RGB LEDs under each button for visual feedback and aesthetics. Here's how to customize them:

### Changing LED Colors

You can change the default colors in the `config.py` file:

```python
# Default LED colors (RGB values)
DEFAULT_COLORS = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "CYAN": (0, 255, 255),
    "MAGENTA": (255, 0, 255),
    "WHITE": (255, 255, 255),
    "OFF": (0, 0, 0)
}
```

Add your own custom colors by adding new entries to this dictionary.

### Changing LED Effects

The button box supports several LED effects that can be customized:

1. **Static**: Solid colors for each LED
2. **Breathing**: Pulsing effect that fades in and out
3. **Rainbow**: Cycling through colors
4. **Reactive**: LEDs light up when buttons are pressed
5. **SimHub**: LEDs controlled by SimHub software

You can modify these effects in the `rgb_leds.py` file or add your own custom effects.

Example of adding a new "alternating" effect:

```python
def alternating_update():
    """Update alternating effect - alternates between two colors"""
    if np is None:
        return
    
    # Calculate based on time
    t = time.ticks_ms() / 500  # Time in 500ms increments
    use_color_1 = (int(t) % 2) == 0
    
    with led_lock:
        for i in range(config.RGB_LED_COUNT):
            # Alternate between two colors based on LED position and time
            if (i % 2 == 0) == use_color_1:
                np[i] = config.DEFAULT_COLORS["RED"]
            else:
                np[i] = config.DEFAULT_COLORS["BLUE"]
        np.write()

# Add to update_effects function
def update_effects():
    # ...existing code...
    elif current_effect == 5:  # New effect ID
        # Alternating effect
        alternating_update()
```

Then add the new effect to the config:

```python
# In config.py
LED_EFFECTS = {
    "STATIC": 0,
    "BREATHING": 1,
    "RAINBOW": 2,
    "REACTIVE": 3,
    "SIMHUB": 4,
    "ALTERNATING": 5  # New effect
}
```

### Button-Specific LED Colors

You can set different colors for specific buttons by modifying the `main.py` file:

```python
# After initializing RGB LEDs in init_all_modules()
# Set different colors for different buttons
rgb_leds.set_button_color(1, config.DEFAULT_COLORS["RED"])
rgb_leds.set_button_color(2, config.DEFAULT_COLORS["GREEN"])
rgb_leds.set_button_color(3, config.DEFAULT_COLORS["BLUE"])
rgb_leds.set_button_color(4, config.DEFAULT_COLORS["YELLOW"])
# ... and so on
```

### SimHub Integration

The RGB LEDs can be controlled by SimHub for game integration. To set this up:

1. Enable WiFi in `config.py`:
   ```python
   WIFI_SSID = "your_wifi_network"
   WIFI_PASSWORD = "your_wifi_password"
   WIFI_ENABLED = True
   ```

2. Enable SimHub integration:
   ```python
   SIMHUB_ENABLED = True
   SIMHUB_PORT = 8888  # UDP port for communication
   ```

3. In SimHub:
   - Install the "Custom Serial" plugin
   - Configure it to send UDP messages to your ESP32's IP address on port 8888
   - Create custom effects that send JSON messages in this format:
     ```json
     {
       "type": "led",
       "leds": [
         {"id": 0, "color": "#FF0000"},
         {"id": 1, "color": "#00FF00"}
       ]
     }
     ```

This allows games to control your button box LEDs based on in-game events (e.g., red for damage, green for healing, etc.).

## Application-Specific Customization

### Gaming

For gaming applications:

- Map buttons to common game controls (WASD, space, etc.)
- Configure rotary encoders for weapon selection or camera control
- Use the funky switch for character movement or menu navigation

### Media Production

For audio/video editing:

- Map buttons to transport controls (play, pause, record, etc.)
- Configure rotary encoders for timeline scrubbing and volume control
- Use the funky switch for tool selection or parameter adjustment

### Productivity

For office applications:

- Map buttons to common shortcuts (copy, paste, save, etc.)
- Configure rotary encoders for scrolling and zoom
- Use the funky switch for window management or tab navigation

## Software Integration

### Windows

On Windows, you can use:

- **JoyToKey**: Map gamepad inputs to keyboard and mouse actions
- **AutoHotkey**: Create complex macros and scripts
- **Antimicro**: Open-source gamepad to keyboard/mouse mapping

### macOS

On macOS, you can use:

- **Enjoyable**: Map gamepad inputs to keyboard and mouse actions
- **Karabiner-Elements**: Remap keyboard inputs and create complex rules
- **BetterTouchTool**: Create custom shortcuts and gestures

### Linux

On Linux, you can use:

- **AntiMicroX**: Map gamepad inputs to keyboard and mouse actions
- **xbindkeys**: Bind commands to input events
- **QJoyPad**: Map joystick buttons to keyboard keys and mouse actions

## Firmware Updates

To update the firmware:

1. Connect to the ESP32 using a serial terminal
2. Upload the new code files
3. Reset the ESP32

You can also implement over-the-air (OTA) updates by enabling WiFi and adding the necessary code to download and apply updates from a server.

## Troubleshooting Customizations

- **Button not working**: Check wiring, pin assignments in `config.py`, and button mapping in `main.py`
- **Encoder behaving erratically**: Adjust debounce settings, check wiring, or try different encoder handling code
- **USB HID not recognized**: Verify USB HID configuration and report descriptor
- **Conflicts with other devices**: Change USB vendor/product IDs in `config.py`
