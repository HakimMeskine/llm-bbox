# ESP32 Button Box - Wiring Diagram

This document provides detailed information about the wiring connections between the ESP32-WROOM-32 microcontroller and all the components in the button box.

## ESP32-WROOM-32 Pinout

The ESP32-WROOM-32 module has the following pinout:

```
                  Antenna
                     │
                 ┌───┘
                 │
     GND ─── 1  │◯│  38 ─── GND
     3V3 ─── 2  │◯│  37 ─── NC
     EN  ─── 3  │◯│  36 ─── SENSOR_VP (GPIO36)
SENSOR_CAPP ─── 4  │◯│  35 ─── SENSOR_VN (GPIO39)
SENSOR_CAPN ─── 5  │◯│  34 ─── GPIO34
     GPIO0 ─── 6  │◯│  33 ─── GPIO35
     GPIO1 ─── 7  │◯│  32 ─── GPIO32
     GPIO2 ─── 8  │◯│  31 ─── GPIO33
     GPIO3 ─── 9  │◯│  30 ─── GPIO25
     GPIO4 ─── 10 │◯│  29 ─── GPIO26
     GPIO5 ─── 11 │◯│  28 ─── GPIO27
     GPIO6 ─── 12 │◯│  27 ─── GPIO14
     GPIO7 ─── 13 │◯│  26 ─── GPIO12
     GPIO8 ─── 14 │◯│  25 ─── GPIO13
     GPIO9 ─── 15 │◯│  24 ─── GPIO15
    GPIO10 ─── 16 │◯│  23 ─── GPIO2
    GPIO11 ─── 17 │◯│  22 ─── GPIO0
     GPIO12 ─── 18 │◯│  21 ─── GPIO4
     GPIO13 ─── 19 │◯│  20 ─── GPIO16
                 └───┘
```

## Button Matrix Wiring

The button matrix consists of 5 rows and 4 columns, for a total of 20 buttons. Each button connects between a row pin and a column pin, with a diode in series to prevent "ghosting".

### Row Pins (Outputs)
- Row 1: GPIO32
- Row 2: GPIO33
- Row 3: GPIO25
- Row 4: GPIO26
- Row 5: GPIO27

### Column Pins (Inputs with Pull-up)
- Column 1: GPIO14
- Column 2: GPIO12
- Column 3: GPIO13
- Column 4: GPIO15

### Button Matrix Schematic

```
        COL1     COL2     COL3     COL4
        GPIO14   GPIO12   GPIO13   GPIO15
          │        │        │        │
ROW1      │        │        │        │
GPIO32 ───┼────────┼────────┼────────┼───
          │        │        │        │
          ▼        ▼        ▼        ▼
         SW1      SW2      SW3      SW4
          │        │        │        │
          │        │        │        │
          └────────┴────────┴────────┘
                      │
                      │
ROW2                  │
GPIO33 ───────────────┼───────────────────
                      │
                      ▼
                     SW5 ... SW8
                      │
                      │
                      └───────────────────
                      │
                      │
ROW3                  │
GPIO25 ───────────────┼───────────────────
                      │
                      ▼
                     SW9 ... SW12
                      │
                      │
                      └───────────────────
                      │
                      │
ROW4                  │
GPIO26 ───────────────┼───────────────────
                      │
                      ▼
                     SW13 ... SW16
                      │
                      │
                      └───────────────────
                      │
                      │
ROW5                  │
GPIO27 ───────────────┼───────────────────
                      │
                      ▼
                     SW17 ... SW20
                      │
                      │
                      └───────────────────
```

Note: Each button has a diode in series (cathode toward the row pin) to prevent "ghosting".

## Rotary Encoder Wiring

### Rotary Encoder 1
- CLK (A): GPIO4
- DT (B): GPIO16
- SW (Push button): GPIO17
- Common: GND

### Rotary Encoder 2
- CLK (A): GPIO5
- DT (B): GPIO18
- SW (Push button): GPIO19
- Common: GND

### Rotary Encoder Schematic

```
           3.3V
            │
            │
            ▼
           10kΩ       10kΩ       10kΩ
            │          │          │
            │          │          │
GPIO4 ──────┴──────────┬──────────┬─────  CLK (A)
                       │          │
                       │          │
GPIO16 ─────────────────┴──────────┬─────  DT (B)
                                  │
                                  │
GPIO17 ────────────────────────────┴─────  SW
                                  │
                                  │
GND ───────────────────────────────┴─────  Common
```

(Similar wiring for Rotary Encoder 2)

## RJXT1F 7-way Encoder (Funky Switch) Wiring

- Up: GPIO21
- Down: GPIO22
- Left: GPIO23
- Right: GPIO2
- Up-Left: GPIO0
- Up-Right: GPIO39
- Down-Left: GPIO35
- Down-Right: GPIO34
- Push button: GPIO36
- Common: GND

### Funky Switch Schematic

```
           3.3V
            │
            ▼
           10kΩ     10kΩ     10kΩ     10kΩ     10kΩ     10kΩ     10kΩ     10kΩ     10kΩ
            │        │        │        │        │        │        │        │        │
            │        │        │        │        │        │        │        │        │
GPIO21 ─────┴────────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┬─────  Up
                     │        │        │        │        │        │        │        │
                     │        │        │        │        │        │        │        │
GPIO22 ──────────────┴────────┬────────┬────────┬────────┬────────┬────────┬────────┬─────  Down
                              │        │        │        │        │        │        │
                              │        │        │        │        │        │        │
GPIO23 ─────────────────────────┴────────┬────────┬────────┬────────┬────────┬────────┬─────  Left
                                        │        │        │        │        │        │
                                        │        │        │        │        │        │
GPIO2 ────────────────────────────────────┴────────┬────────┬────────┬────────┬────────┬─────  Right
                                                  │        │        │        │        │
                                                  │        │        │        │        │
GPIO0 ─────────────────────────────────────────────┴────────┬────────┬────────┬────────┬─────  Up-Left
                                                           │        │        │        │
                                                           │        │        │        │
GPIO39 ──────────────────────────────────────────────────────┴────────┬────────┬────────┬─────  Up-Right
                                                                     │        │        │
                                                                     │        │        │
GPIO35 ─────────────────────────────────────────────────────────────────┴────────┬────────┬─────  Down-Left
                                                                               │        │
                                                                               │        │
GPIO34 ──────────────────────────────────────────────────────────────────────────┴────────┬─────  Down-Right
                                                                                         │
                                                                                         │
GPIO36 ────────────────────────────────────────────────────────────────────────────────────┴─────  Push button
                                                                                         │
                                                                                         │
GND ──────────────────────────────────────────────────────────────────────────────────────┴─────  Common
```

## Status LED Wiring

- Status LED 1: GPIO10 → 330Ω resistor → LED → GND
- Status LED 2: GPIO9 → 330Ω resistor → LED → GND

## RGB LED Wiring

The button box includes 20 WS2812B RGB LEDs (one under each button) connected in a daisy chain configuration. The data signal from the ESP32 passes through a level shifter to convert from 3.3V to 5V logic.

### RGB LED Data Connection

- ESP32 GPIO3 → 74HCT245 Level Shifter → 100Ω resistor → LED1 DIN
- LED1 DOUT → LED2 DIN
- LED2 DOUT → LED3 DIN
- ...and so on for all 20 LEDs

### Level Shifter Connections

```
                 VCC (5V)
                    │
                    ▼
                 ┌─────┐
                 │     │
ESP32 GPIO3 ──── │A1 B1│ ──── 100Ω ──── LED1 DIN
                 │     │
                 │     │
ESP32 3.3V ───── │VccA │
                 │     │
                 │     │
5V ────────────── │VccB │
                 │     │
                 │     │
GND ───────────── │GND  │
                 │     │
                 │     │
ESP32 3.3V ───── │DIR  │
                 │     │
                 │     │
ESP32 3.3V ───── │OE   │
                 │     │
                 └─────┘
                74HCT245
```

### RGB LED Power Connections

All RGB LEDs share common power connections:

- 5V → 100μF capacitor → 10μF capacitor → LED1 VCC, LED2 VCC, ..., LED20 VCC
- GND → LED1 GND, LED2 GND, ..., LED20 GND

### RGB LED Schematic

```
     5V
     │
     ▼
  100μF   10μF
     │      │
     │      │
     └──────┴───────┬───────────┬─────────── ... ───┬─────────── VCC
                    │           │                   │
                    ▼           ▼                   ▼
                   LED1        LED2                LED20
                    │           │                   │
     ESP32          │           │                   │
     GPIO3          │           │                   │
       │            │           │                   │
       ▼            │           │                   │
   74HCT245         │           │                   │
       │            │           │                   │
       ▼            │           │                   │
     100Ω           │           │                   │
       │            │           │                   │
       ▼            │           │                   │
      DIN          DOUT        DOUT                DOUT
       │            │           │                   │
       │            │           │                   │
       └────────────►           │                   │
                    │           │                   │
                    └───────────►                   │
                                                    │
                                ... ────────────────►
                                │
                                │
     GND ────────────────────────┴───────────┴─────────── ... ───┴─────────── GND
```

## Power Supply

The ESP32 is powered via the USB-C connector, which provides 5V. A voltage regulator (AMS1117-3.3) converts this to 3.3V for the ESP32 and other components. The 5V from USB is also used directly to power the RGB LEDs.

```
                                                 ┌─── To RGB LEDs (VCC)
                                                 │
                                                 │
USB-C 5V ──────┬─────────────────────────────────┴─────────────────────────
               │
               │
               ▼
            AMS1117
               │
               │
               ▼
3.3V ──────────┬─────────────────────────────────────────────────
               │                                   │
               │                                   │
               ▼                                   │
           0.1μF Cap                               │
               │                                   │
               │                                   │
               ▼                                   ▼
GND ───────────┴───────────────────────────────────┴─────────────────────────
                                                   │
                                                   │
                                                   └─── To RGB LEDs (GND)
```

### Power Considerations for RGB LEDs

- Each WS2812B LED can draw up to 60mA at full brightness (white)
- With 20 LEDs, the total current could reach 1.2A at maximum brightness
- The USB-C connector can typically provide up to 3A, which is sufficient
- Power filtering capacitors (100μF, 10μF) are added near the RGB LEDs to stabilize the power supply
- Wide traces (1.0mm minimum) are used for the 5V and GND connections to the RGB LEDs

## Programming Interface

- Reset button: ESP32 EN pin → button → GND
- Boot button: ESP32 GPIO0 → button → GND

## Complete Wiring Diagram

The complete wiring diagram combines all of the above connections. Due to the complexity, it's recommended to follow the PCB layout for the actual implementation.

## Notes

1. All inputs (column pins, encoder pins, funky switch pins) use internal pull-up resistors enabled in software.
2. External pull-up resistors (10kΩ) are recommended for the rotary encoders and funky switch for better reliability.
3. Decoupling capacitors (0.1μF) should be placed near the ESP32 power pins and the voltage regulator.
4. The diodes in the button matrix should be oriented with the cathode (band) toward the row pin.
