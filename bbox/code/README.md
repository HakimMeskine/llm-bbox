# ESP32 Button Box - Code Documentation

This directory contains the MicroPython code for the ESP32 button box. The code handles the button matrix, rotary encoders, and funky switch, and sends the input data to the host computer via USB HID.

## Files Overview

- `boot.py`: Runs when the ESP32 boots up, sets up USB, WiFi, and Bluetooth if enabled
- `main.py`: Main application entry point, handles the main loop and input processing
- `config.py`: Configuration file with pin assignments and other settings
- `button_matrix.py`: Handles the 5x4 button matrix
- `rotary_encoders.py`: Handles the two rotary encoders and their push buttons
- `funky_switch.py`: Handles the RJXT1F 7-way encoder (funky switch)
- `usb_hid.py`: Handles USB HID functionality for sending input data to the host computer
- `rgb_leds.py`: Controls the WS2812B RGB LEDs and provides various lighting effects

## Setting Up MicroPython on ESP32

1. **Install esptool**: 
   ```
   pip install esptool
   ```

2. **Download MicroPython firmware**:
   Download the latest MicroPython firmware for ESP32 from the [official website](https://micropython.org/download/esp32/).

3. **Erase the ESP32 flash**:
   ```
   esptool.py --port /dev/ttyUSB0 erase_flash
   ```
   (Replace `/dev/ttyUSB0` with the appropriate port for your system)

4. **Flash MicroPython firmware**:
   ```
   esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin
   ```
   (Replace the firmware filename with the one you downloaded)

## Uploading the Code

There are several tools you can use to upload the code to the ESP32:

### Using Thonny IDE

1. Install [Thonny IDE](https://thonny.org/)
2. Connect your ESP32 to your computer
3. Open Thonny and select "MicroPython (ESP32)" in the interpreter settings
4. Upload each file to the ESP32 using the "File > Save as..." menu and selecting "MicroPython device"

### Using ampy

1. Install ampy:
   ```
   pip install adafruit-ampy
   ```

2. Upload all files:
   ```
   ampy --port /dev/ttyUSB0 put boot.py
   ampy --port /dev/ttyUSB0 put main.py
   ampy --port /dev/ttyUSB0 put config.py
   ampy --port /dev/ttyUSB0 put button_matrix.py
   ampy --port /dev/ttyUSB0 put rotary_encoders.py
   ampy --port /dev/ttyUSB0 put funky_switch.py
   ampy --port /dev/ttyUSB0 put usb_hid.py
   ampy --port /dev/ttyUSB0 put rgb_leds.py
   ```

## Configuration

The `config.py` file contains all the pin assignments and configuration parameters. You may need to adjust these based on your specific wiring and requirements:

- Pin assignments for the button matrix, rotary encoders, funky switch, and RGB LEDs
- Debounce times and scan intervals
- USB HID configuration
- RGB LED effects and colors
- SimHub integration settings
- WiFi and Bluetooth settings (if needed)

## Usage

Once the code is uploaded to the ESP32 and the button box is assembled, it will function as a USB HID device:

1. Connect the ESP32 button box to your computer via USB
2. The device should be recognized as a USB HID device (gamepad/controller)
3. The buttons, rotary encoders, and funky switch will send input events to the computer
4. You can use software like [JoyToKey](https://joytokey.net/) or [antimicro](https://github.com/AntiMicro/antimicro) to map these inputs to keyboard keys or mouse movements

## Debugging

If you need to debug the button box:

1. Connect to the ESP32 using a serial terminal (115200 baud)
2. The code includes print statements that output debug information
3. The status LEDs provide visual feedback:
   - LED1: Heartbeat indicator (blinks when the code is running)
   - LED2: Blinks when a button is pressed

## Customization

You can customize the behavior of the button box by modifying the code:

- Change the button mapping in `main.py`
- Adjust the debounce times in `config.py`
- Modify the USB HID report descriptor in `usb_hid.py` to change how the device appears to the host computer
- Customize RGB LED effects and colors in `rgb_leds.py` and `config.py`
- Set up SimHub integration for game-controlled lighting effects

### RGB LED Features

The RGB LED module (`rgb_leds.py`) provides the following features:

- Individual control of 20 WS2812B RGB LEDs (one under each button)
- Multiple lighting effects:
  - Static: Solid colors
  - Breathing: Pulsing effect
  - Rainbow: Cycling through colors
  - Reactive: LEDs light up when buttons are pressed
  - SimHub: LEDs controlled by SimHub software
- Button-specific color mapping
- Brightness control
- SimHub integration via WiFi for game-controlled lighting

See the `customization_guide.md` for detailed information on customizing the RGB LED functionality.
