# ESP32 Button Box

This project contains the design files and code for a button box based on the ESP32-WROOM-32 microcontroller. The button box features 20 push buttons arranged in a 5x4 grid, 2 rotary encoders with push buttons, and 1 RJXT1F 7-way encoder (funky switch) with push button.

```
+-----------------------------------------------------+
|                  ESP32 BUTTON BOX                   |
+-----------------------------------------------------+
|                                                     |
|  [B01] [B02] [B03] [B04]        +---+      +---+   |
|                                  |ENC|      |ENC|   |
|  [B05] [B06] [B07] [B08]        | 1 |      | 2 |   |
|                                  +---+      +---+   |
|  [B09] [B10] [B11] [B12]                           |
|                                                     |
|  [B13] [B14] [B15] [B16]                           |
|                                      +-------+      |
|  [B17] [B18] [B19] [B20]            | FUNKY |      |
|                                      +-------+      |
|                                                     |
|  [LED1]                             [LED2]          |
|                                                     |
+-----------------------------------------------------+
|                    USB-C PORT                       |
+-----------------------------------------------------+
```
*ASCII art representation of the button box layout*

## Overview

This button box is designed to be a versatile input device that can be used for various applications such as:

- Gaming (flight simulators, racing games, etc.)
- Media production (audio/video editing)
- Productivity (custom keyboard shortcuts)
- Industrial control
- Home automation

The device connects to a computer via USB and appears as a standard HID (Human Interface Device) gamepad/controller, making it compatible with most operating systems without requiring special drivers.

## Features

- **20 Push Buttons**: Arranged in a 5x4 grid for easy access
- **2 Rotary Encoders**: With push button functionality for additional inputs
- **RJXT1F 7-way Encoder**: Provides directional control and push button
- **RGB LEDs**: Individual RGB LED under each button for customizable lighting effects
- **USB HID Interface**: Plug-and-play with any computer
- **SimHub Integration**: Control RGB LEDs through SimHub for game integration
- **Customizable**: Fully programmable using MicroPython
- **Status LEDs**: Visual feedback for device status
- **Open Source**: All design files and code are freely available

## Directory Structure

- `/pcb`: PCB design files and manufacturing information
  - `schematic_description.txt`: Detailed description of the circuit schematic
  - `pcb_layout_description.txt`: PCB layout guidelines and considerations
  - `bill_of_materials.csv`: List of all components needed
  - `manufacturing_guide.md`: Guide for PCB manufacturing

- `/code`: MicroPython code for the ESP32
  - `boot.py`: Initial boot configuration
  - `main.py`: Main application code
  - `config.py`: Configuration parameters
  - `button_matrix.py`: Button matrix handling
  - `rotary_encoders.py`: Rotary encoder handling
  - `funky_switch.py`: Funky switch handling
  - `usb_hid.py`: USB HID functionality
  - `rgb_leds.py`: RGB LED control and effects
  - `README.md`: Code documentation

- `/docs`: Documentation and reference materials
  - `assembly_guide.md`: Step-by-step assembly instructions
  - `wiring_diagram.md`: Detailed wiring information
  - `customization_guide.md`: Guide for customizing the button box

## Getting Started

1. **PCB Manufacturing**: 
   - Review the files in the `/pcb` directory
   - Follow the instructions in `manufacturing_guide.md` to prepare files for PCB manufacturing
   - Order the PCB from a manufacturer like PCBway

2. **Component Sourcing**:
   - Use the `bill_of_materials.csv` to source all required components
   - Ensure you get the correct specifications for each component

3. **Assembly**:
   - Follow the `assembly_guide.md` for step-by-step instructions
   - Refer to `wiring_diagram.md` for detailed connection information

4. **Programming**:
   - Follow the instructions in the code `README.md` to set up MicroPython
   - Upload all the code files to the ESP32

5. **Customization**:
   - Refer to `customization_guide.md` to adapt the button box to your specific needs

## PCB Manufacturing

The PCB design files are provided in formats compatible with PCB manufacturers like PCBway. The design uses a 2-layer PCB with standard FR-4 material. Detailed manufacturing specifications are provided in the `manufacturing_guide.md` file.

## Programming

The button box uses MicroPython, a lean implementation of Python 3 specifically for microcontrollers. The code is modular and well-documented, making it easy to understand and customize. Detailed programming instructions are provided in the code `README.md` file.

## Customization

The button box is designed to be highly customizable. You can:

- Modify the button mapping to suit your specific application
- Change the behavior of buttons, rotary encoders, and the funky switch
- Add additional features like RGB LEDs or an OLED display
- Create custom enclosures to match your aesthetic preferences

Refer to `customization_guide.md` for detailed information on customizing your button box.

## License

This project is released under the MIT License. See the LICENSE file for details.

## Contributing

Contributions to this project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## Acknowledgments

- Thanks to the MicroPython community for their excellent work
- Thanks to the open-source hardware community for inspiration and resources
