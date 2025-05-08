# ESP32 Button Box - Funky Switch Module
# This module handles the RJXT1F 7-way encoder (funky switch)

import machine
import time
import config

# Funky switch state tracking
last_direction = None
button_state = False
last_button_time = 0

# Direction pins
up_pin = None
down_pin = None
left_pin = None
right_pin = None
up_left_pin = None
up_right_pin = None
down_left_pin = None
down_right_pin = None
sw_pin = None

# Direction constants
DIRECTION_NONE = "NONE"
DIRECTION_UP = "UP"
DIRECTION_DOWN = "DOWN"
DIRECTION_LEFT = "LEFT"
DIRECTION_RIGHT = "RIGHT"
DIRECTION_UP_LEFT = "UP_LEFT"
DIRECTION_UP_RIGHT = "UP_RIGHT"
DIRECTION_DOWN_LEFT = "DOWN_LEFT"
DIRECTION_DOWN_RIGHT = "DOWN_RIGHT"
DIRECTION_BUTTON = "BUTTON"

def init():
    """Initialize the funky switch pins"""
    global up_pin, down_pin, left_pin, right_pin
    global up_left_pin, up_right_pin, down_left_pin, down_right_pin, sw_pin
    
    # Initialize direction pins as inputs with pull-up
    up_pin = machine.Pin(config.FUNKY_UP_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    down_pin = machine.Pin(config.FUNKY_DOWN_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    left_pin = machine.Pin(config.FUNKY_LEFT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    right_pin = machine.Pin(config.FUNKY_RIGHT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    up_left_pin = machine.Pin(config.FUNKY_UP_LEFT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    up_right_pin = machine.Pin(config.FUNKY_UP_RIGHT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    down_left_pin = machine.Pin(config.FUNKY_DOWN_LEFT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    down_right_pin = machine.Pin(config.FUNKY_DOWN_RIGHT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    
    # Initialize push button pin
    sw_pin = machine.Pin(config.FUNKY_SW_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

def read_direction():
    """Read the current direction of the funky switch"""
    # Check each direction pin (active low)
    if up_pin.value() == 0:
        return DIRECTION_UP
    elif down_pin.value() == 0:
        return DIRECTION_DOWN
    elif left_pin.value() == 0:
        return DIRECTION_LEFT
    elif right_pin.value() == 0:
        return DIRECTION_RIGHT
    elif up_left_pin.value() == 0:
        return DIRECTION_UP_LEFT
    elif up_right_pin.value() == 0:
        return DIRECTION_UP_RIGHT
    elif down_left_pin.value() == 0:
        return DIRECTION_DOWN_LEFT
    elif down_right_pin.value() == 0:
        return DIRECTION_DOWN_RIGHT
    else:
        return DIRECTION_NONE

def check_direction_change():
    """Check if the direction has changed and return the new direction"""
    global last_direction
    
    current_direction = read_direction()
    
    # If direction changed
    if current_direction != last_direction:
        # Debounce
        time.sleep_ms(5)  # 5ms debounce
        
        # Read again to confirm
        current_direction = read_direction()
        
        if current_direction != last_direction:
            # Update last direction
            last_direction = current_direction
            
            # Only return a direction if it's not NONE
            if current_direction != DIRECTION_NONE:
                return current_direction
    
    return None

def check_button():
    """Check if the funky switch button is pressed"""
    global button_state, last_button_time
    
    current_time = time.ticks_ms()
    
    # Check button (active low)
    if sw_pin.value() == 0:
        # Debounce
        if time.ticks_diff(current_time, last_button_time) > config.DEBOUNCE_TIME_MS:
            if not button_state:
                button_state = True
                last_button_time = current_time
                return True
    else:
        button_state = False
    
    return False

def get_current_state():
    """Get the current state of the funky switch (direction and button)"""
    direction = read_direction()
    button_pressed = (sw_pin.value() == 0)
    
    return {
        "direction": direction,
        "button_pressed": button_pressed
    }

def is_direction_active(direction):
    """Check if a specific direction is currently active"""
    return read_direction() == direction

def is_button_pressed():
    """Check if the button is currently pressed"""
    return sw_pin.value() == 0
