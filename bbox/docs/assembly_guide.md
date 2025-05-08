# ESP32 Button Box - Assembly Guide

This guide provides step-by-step instructions for assembling the ESP32 button box after you've received the PCB from the manufacturer.

## Required Tools

- Soldering iron (temperature-controlled recommended)
- Solder (lead-free, 0.5-0.7mm diameter recommended)
- Flux
- Tweezers
- Magnifying glass or loupe
- Multimeter
- Wire cutters
- Wire strippers
- Heat shrink tubing (various sizes)
- Hot air gun or lighter (for heat shrink)
- Isopropyl alcohol (for cleaning)
- Cotton swabs
- Screwdriver set
- Needle-nose pliers

## Required Materials

- Manufactured PCB
- All components listed in the Bill of Materials
- Enclosure (3D printed or purchased)
- M3 screws and nuts (for mounting)
- USB-C cable
- Knobs for rotary encoders
- Cap for funky switch

## Assembly Steps

### 1. Prepare Your Workspace

- Ensure you have a clean, well-lit workspace
- Have all tools and components organized and ready
- Use an anti-static mat and wrist strap if available

### 2. Inspect the PCB

- Check for any manufacturing defects
- Verify that all holes and pads are clean
- Compare with the design files to ensure everything matches

### 3. Solder Components (in recommended order)

#### 3.1. SMD Components

1. **Voltage Regulator (U2)**
   - Apply a small amount of solder to one pad
   - Position the component using tweezers
   - Reheat the pad to secure the component in place
   - Solder the remaining pins

2. **Resistors and Capacitors**
   - Follow the same process as the voltage regulator
   - Pay attention to the orientation of polarized capacitors

3. **USB-C Connector (J1)**
   - Apply flux to the pads
   - Align the connector carefully
   - Solder one pin to hold it in place
   - Check alignment and adjust if necessary
   - Solder the remaining pins

#### 3.2. Through-Hole Components

1. **ESP32-WROOM-32 Module (U1)**
   - Insert the module into the PCB
   - Ensure it's fully seated and properly aligned
   - Solder one pin to hold it in place
   - Check alignment and adjust if necessary
   - Solder the remaining pins

2. **Diodes (D1-D20)**
   - Pay attention to the orientation (cathode band)
   - Insert all diodes
   - Bend the leads slightly to hold them in place
   - Solder all pins
   - Trim excess leads

3. **Push Buttons (SW1-SW20, SW21, SW22)**
   - Insert the buttons into their positions
   - Ensure they're fully seated and level
   - Solder one pin of each button
   - Check alignment and adjust if necessary
   - Solder the remaining pins

4. **Rotary Encoders (ENC1, ENC2)**
   - Insert the encoders into their positions
   - Ensure they're fully seated and level
   - Solder one pin of each encoder
   - Check alignment and adjust if necessary
   - Solder the remaining pins

5. **Funky Switch (ENC3)**
   - Insert the funky switch into its position
   - Ensure it's fully seated and level
   - Solder one pin
   - Check alignment and adjust if necessary
   - Solder the remaining pins

6. **Status LEDs (LED1, LED2)**
   - Pay attention to the orientation (anode/cathode)
   - Insert the LEDs
   - Bend the leads slightly to hold them in place
   - Solder all pins
   - Trim excess leads

### 4. Clean the PCB

- Use isopropyl alcohol and cotton swabs to clean flux residue
- Inspect all solder joints for quality
- Check for and fix any solder bridges or cold joints

### 5. Initial Testing

- Perform continuity tests with a multimeter
- Check for shorts between power and ground
- Check for proper connections between components

### 6. Prepare the Enclosure

- If using a 3D printed enclosure, clean up any printing artifacts
- Drill or modify as needed for mounting holes, USB port, etc.
- Test fit the PCB in the enclosure

### 7. Flash MicroPython and Upload Code

- Follow the instructions in the code README to flash MicroPython
- Upload all the code files to the ESP32

### 8. Final Assembly

1. Mount the PCB in the enclosure using M3 screws and nuts
2. Attach knobs to the rotary encoders
3. Attach cap to the funky switch
4. Secure the enclosure with screws

### 9. Final Testing

- Connect the button box to a computer via USB
- Verify that it's recognized as a USB HID device
- Test all buttons, rotary encoders, and the funky switch
- Verify that the status LEDs work correctly

## Troubleshooting

### Common Issues and Solutions

1. **Button not registering**
   - Check solder joints
   - Verify diode orientation
   - Check for broken traces on the PCB

2. **Rotary encoder not working**
   - Check solder joints
   - Verify pin connections in the code
   - Test with a multimeter in continuity mode

3. **USB not recognized**
   - Check USB connector solder joints
   - Verify USB-C cable is working
   - Check voltage regulator output (should be 3.3V)

4. **ESP32 not booting**
   - Check power connections
   - Verify that the ESP32 module is properly soldered
   - Try reflashing MicroPython

5. **Funky switch not working**
   - Check solder joints
   - Verify pin connections in the code
   - Test with a multimeter in continuity mode

## Maintenance

- Keep the button box clean and free of dust
- Periodically check all connections and solder joints
- Update the firmware as needed

## Safety Considerations

- Always disconnect the button box from USB before opening the enclosure
- Be careful when handling the PCB to avoid static discharge
- Keep the button box away from liquids and extreme temperatures
