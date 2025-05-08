# ESP32 Button Box - Button Matrix Module
# This module handles the button matrix scanning and debouncing

import machine
import time
import config

# Button state tracking
button_states = {}  # Dictionary to track button states
last_press_time = {}  # Dictionary to track last press time for debouncing

def init():
    """Initialize the button matrix pins"""
    global row_pins, col_pins
    
    # Initialize row pins as outputs
    row_pins = []
    for pin in config.ROW_PINS:
        row_pin = machine.Pin(pin, machine.Pin.OUT)
        row_pin.value(1)  # Set high by default
        row_pins.append(row_pin)
    
    # Initialize column pins as inputs with pull-up
    col_pins = []
    for pin in config.COL_PINS:
        col_pin = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
        col_pins.append(col_pin)
    
    # Initialize button states
    for row in range(len(config.BUTTON_MAP)):
        for col in range(len(config.BUTTON_MAP[0])):
            button_num = config.BUTTON_MAP[row][col]
            button_states[button_num] = False
            last_press_time[button_num] = 0

def scan():
    """Scan the button matrix and return a list of pressed buttons"""
    pressed_buttons = []
    
    # Scan each row
    for row_idx, row_pin in enumerate(row_pins):
        # Set the current row pin low
        row_pin.value(0)
        
        # Small delay to allow pin state to settle
        time.sleep_us(10)
        
        # Check each column in this row
        for col_idx, col_pin in enumerate(col_pins):
            # If column reads low, the button at this row/col is pressed
            if col_pin.value() == 0:
                button_num = config.BUTTON_MAP[row_idx][col_idx]
                
                # Debounce check
                current_time = time.ticks_ms()
                if (time.ticks_diff(current_time, last_press_time.get(button_num, 0)) 
                        > config.DEBOUNCE_TIME_MS):
                    
                    # If button state changed from not pressed to pressed
                    if not button_states[button_num]:
                        button_states[button_num] = True
                        pressed_buttons.append(button_num)
                        last_press_time[button_num] = current_time
            else:
                # Button is not pressed
                button_num = config.BUTTON_MAP[row_idx][col_idx]
                if button_states[button_num]:
                    button_states[button_num] = False
        
        # Set the row pin back high
        row_pin.value(1)
    
    return pressed_buttons

def is_pressed(button_num):
    """Check if a specific button is currently pressed"""
    return button_states.get(button_num, False)

def get_all_states():
    """Return the current state of all buttons"""
    return button_states.copy()

def reset_states():
    """Reset all button states to not pressed"""
    for button_num in button_states:
        button_states[button_num] = False
