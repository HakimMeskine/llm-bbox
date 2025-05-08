# ESP32 Button Box - USB HID Module
# This module handles USB HID functionality

import config
import time

# Try to import the USB HID module
try:
    import usb_hid
    from usb.core import USBError
    HID_AVAILABLE = True
except ImportError:
    print("USB HID module not available. Running in debug mode.")
    HID_AVAILABLE = False

# HID report descriptor for a generic gamepad/controller
# This defines a device with:
# - 32 buttons
# - 8 axes (X, Y, Z, Rx, Ry, Rz, Slider1, Slider2)
GAMEPAD_REPORT_DESCRIPTOR = bytes([
    0x05, 0x01,        # Usage Page (Generic Desktop Ctrls)
    0x09, 0x05,        # Usage (Game Pad)
    0xA1, 0x01,        # Collection (Application)
    0x85, 0x01,        #   Report ID (1)
    
    # Buttons (32 buttons)
    0x05, 0x09,        #   Usage Page (Button)
    0x19, 0x01,        #   Usage Minimum (0x01)
    0x29, 0x20,        #   Usage Maximum (0x20)
    0x15, 0x00,        #   Logical Minimum (0)
    0x25, 0x01,        #   Logical Maximum (1)
    0x75, 0x01,        #   Report Size (1)
    0x95, 0x20,        #   Report Count (32)
    0x81, 0x02,        #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    
    # Axes (8 axes: X, Y, Z, Rx, Ry, Rz, Slider1, Slider2)
    0x05, 0x01,        #   Usage Page (Generic Desktop Ctrls)
    0x09, 0x30,        #   Usage (X)
    0x09, 0x31,        #   Usage (Y)
    0x09, 0x32,        #   Usage (Z)
    0x09, 0x33,        #   Usage (Rx)
    0x09, 0x34,        #   Usage (Ry)
    0x09, 0x35,        #   Usage (Rz)
    0x09, 0x36,        #   Usage (Slider)
    0x09, 0x36,        #   Usage (Slider)
    0x15, 0x00,        #   Logical Minimum (0)
    0x26, 0xFF, 0x00,  #   Logical Maximum (255)
    0x75, 0x08,        #   Report Size (8)
    0x95, 0x08,        #   Report Count (8)
    0x81, 0x02,        #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    
    0xC0,              # End Collection
])

# HID device
hid_device = None

# Button state tracking
button_states = bytearray(4)  # 32 buttons = 4 bytes
axis_states = bytearray(8)    # 8 axes = 8 bytes

def init():
    """Initialize the USB HID functionality"""
    global hid_device
    
    if not config.USB_ENABLED or not HID_AVAILABLE:
        print("USB HID functionality disabled or not available")
        return False
    
    try:
        # Create HID device
        hid_device = usb_hid.Device(
            descriptor=GAMEPAD_REPORT_DESCRIPTOR,
            report_ids=(1,),
            usage_page=0x01,  # Generic Desktop Controls
            usage=0x05,       # Game Pad
            in_report_lengths=(13,),  # 1 report ID + 4 button bytes + 8 axis bytes
            out_report_lengths=(0,)
        )
        
        # Register the device
        usb_hid.enable((hid_device,))
        
        print("USB HID device initialized")
        return True
    except Exception as e:
        print(f"Error initializing USB HID: {e}")
        return False

def set_button(button_num, pressed):
    """Set the state of a button (1-32)"""
    if not config.USB_ENABLED or not HID_AVAILABLE or not hid_device:
        return False
    
    if button_num < 1 or button_num > 32:
        return False
    
    # Adjust button_num to be 0-based
    button_idx = button_num - 1
    
    # Calculate byte index and bit position
    byte_idx = button_idx // 8
    bit_pos = button_idx % 8
    
    # Set or clear the bit
    if pressed:
        button_states[byte_idx] |= (1 << bit_pos)
    else:
        button_states[byte_idx] &= ~(1 << bit_pos)
    
    return True

def set_axis(axis_num, value):
    """Set the value of an axis (1-8)"""
    if not config.USB_ENABLED or not HID_AVAILABLE or not hid_device:
        return False
    
    if axis_num < 1 or axis_num > 8:
        return False
    
    # Adjust axis_num to be 0-based
    axis_idx = axis_num - 1
    
    # Set the axis value (0-255)
    axis_states[axis_idx] = value & 0xFF
    
    return True

def send_report():
    """Send the HID report with the current button and axis states"""
    if not config.USB_ENABLED or not HID_AVAILABLE or not hid_device:
        return False
    
    try:
        # Combine report ID, button states, and axis states
        report = bytearray([0x01]) + button_states + axis_states
        
        # Send the report
        hid_device.send_report(report)
        return True
    except USBError as e:
        print(f"USB error when sending report: {e}")
        return False
    except Exception as e:
        print(f"Error sending HID report: {e}")
        return False

def clear_all_buttons():
    """Clear all button states"""
    global button_states
    button_states = bytearray(4)  # Reset to all zeros

def center_all_axes():
    """Center all axes (set to 128)"""
    global axis_states
    axis_states = bytearray([128] * 8)  # Set all axes to center position

def reset_all():
    """Reset all button and axis states"""
    clear_all_buttons()
    center_all_axes()
    send_report()
