# ESP32 Button Box - Rotary Encoders Module
# This module handles the rotary encoders and their push buttons

import machine
import time
import config

# Encoder state tracking
encoder1_value = 0
encoder2_value = 0
encoder1_last_state = 0
encoder2_last_state = 0
encoder1_button_state = False
encoder2_button_state = False
encoder1_last_button_time = 0
encoder2_last_button_time = 0

# Encoder pins
encoder1_clk = None
encoder1_dt = None
encoder1_sw = None
encoder2_clk = None
encoder2_dt = None
encoder2_sw = None

def init():
    """Initialize the rotary encoder pins"""
    global encoder1_clk, encoder1_dt, encoder1_sw
    global encoder2_clk, encoder2_dt, encoder2_sw
    global encoder1_last_state, encoder2_last_state
    
    # Initialize Encoder 1 pins
    encoder1_clk = machine.Pin(config.ENCODER1_CLK_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    encoder1_dt = machine.Pin(config.ENCODER1_DT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    encoder1_sw = machine.Pin(config.ENCODER1_SW_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    
    # Initialize Encoder 2 pins
    encoder2_clk = machine.Pin(config.ENCODER2_CLK_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    encoder2_dt = machine.Pin(config.ENCODER2_DT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    encoder2_sw = machine.Pin(config.ENCODER2_SW_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    
    # Read initial states
    encoder1_last_state = (encoder1_clk.value() << 1) | encoder1_dt.value()
    encoder2_last_state = (encoder2_clk.value() << 1) | encoder2_dt.value()

def read_encoder1():
    """Read encoder 1 and return change in value (-1, 0, or 1)"""
    global encoder1_value, encoder1_last_state
    
    # Read current state
    clk_state = encoder1_clk.value()
    dt_state = encoder1_dt.value()
    current_state = (clk_state << 1) | dt_state
    
    # If state changed
    if current_state != encoder1_last_state:
        # Debounce
        time.sleep_us(1000)  # 1ms debounce
        
        # Read again to confirm
        clk_state = encoder1_clk.value()
        dt_state = encoder1_dt.value()
        current_state = (clk_state << 1) | dt_state
        
        if current_state != encoder1_last_state:
            # Determine direction based on state transition
            if (encoder1_last_state == 0b00 and current_state == 0b01) or \
               (encoder1_last_state == 0b01 and current_state == 0b11) or \
               (encoder1_last_state == 0b11 and current_state == 0b10) or \
               (encoder1_last_state == 0b10 and current_state == 0b00):
                encoder1_value += 1
                result = 1
            elif (encoder1_last_state == 0b00 and current_state == 0b10) or \
                 (encoder1_last_state == 0b10 and current_state == 0b11) or \
                 (encoder1_last_state == 0b11 and current_state == 0b01) or \
                 (encoder1_last_state == 0b01 and current_state == 0b00):
                encoder1_value -= 1
                result = -1
            else:
                # Invalid transition, likely due to noise
                result = 0
            
            encoder1_last_state = current_state
            return result
    
    return 0  # No change

def read_encoder2():
    """Read encoder 2 and return change in value (-1, 0, or 1)"""
    global encoder2_value, encoder2_last_state
    
    # Read current state
    clk_state = encoder2_clk.value()
    dt_state = encoder2_dt.value()
    current_state = (clk_state << 1) | dt_state
    
    # If state changed
    if current_state != encoder2_last_state:
        # Debounce
        time.sleep_us(1000)  # 1ms debounce
        
        # Read again to confirm
        clk_state = encoder2_clk.value()
        dt_state = encoder2_dt.value()
        current_state = (clk_state << 1) | dt_state
        
        if current_state != encoder2_last_state:
            # Determine direction based on state transition
            if (encoder2_last_state == 0b00 and current_state == 0b01) or \
               (encoder2_last_state == 0b01 and current_state == 0b11) or \
               (encoder2_last_state == 0b11 and current_state == 0b10) or \
               (encoder2_last_state == 0b10 and current_state == 0b00):
                encoder2_value += 1
                result = 1
            elif (encoder2_last_state == 0b00 and current_state == 0b10) or \
                 (encoder2_last_state == 0b10 and current_state == 0b11) or \
                 (encoder2_last_state == 0b11 and current_state == 0b01) or \
                 (encoder2_last_state == 0b01 and current_state == 0b00):
                encoder2_value -= 1
                result = -1
            else:
                # Invalid transition, likely due to noise
                result = 0
            
            encoder2_last_state = current_state
            return result
    
    return 0  # No change

def check_encoder_buttons():
    """Check the encoder push buttons and return a list of pressed buttons"""
    global encoder1_button_state, encoder2_button_state
    global encoder1_last_button_time, encoder2_last_button_time
    
    pressed_buttons = []
    current_time = time.ticks_ms()
    
    # Check Encoder 1 button
    if encoder1_sw.value() == 0:  # Button is active low
        # Debounce
        if time.ticks_diff(current_time, encoder1_last_button_time) > config.DEBOUNCE_TIME_MS:
            if not encoder1_button_state:
                encoder1_button_state = True
                pressed_buttons.append("ENCODER1_BUTTON")
                encoder1_last_button_time = current_time
    else:
        encoder1_button_state = False
    
    # Check Encoder 2 button
    if encoder2_sw.value() == 0:  # Button is active low
        # Debounce
        if time.ticks_diff(current_time, encoder2_last_button_time) > config.DEBOUNCE_TIME_MS:
            if not encoder2_button_state:
                encoder2_button_state = True
                pressed_buttons.append("ENCODER2_BUTTON")
                encoder2_last_button_time = current_time
    else:
        encoder2_button_state = False
    
    return pressed_buttons

def get_encoder1_value():
    """Get the current value of encoder 1"""
    return encoder1_value

def get_encoder2_value():
    """Get the current value of encoder 2"""
    return encoder2_value

def reset_encoder_values():
    """Reset both encoder values to zero"""
    global encoder1_value, encoder2_value
    encoder1_value = 0
    encoder2_value = 0
