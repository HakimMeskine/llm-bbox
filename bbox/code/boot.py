# ESP32 Button Box - Boot Script
# This script runs when the ESP32 first boots up

import machine
import time
import config

# Try to import USB-related modules
try:
    import usb_core
    import usb_hid
    USB_AVAILABLE = True
except ImportError:
    print("USB modules not available")
    USB_AVAILABLE = False

def setup_usb():
    """Set up the USB interface"""
    if not USB_AVAILABLE or not config.USB_ENABLED:
        print("USB functionality disabled or not available")
        return False
    
    try:
        # Configure USB device
        usb_core.init(
            vid=config.USB_VENDOR_ID,
            pid=config.USB_PRODUCT_ID,
            manufacturer=config.USB_MANUFACTURER,
            product=config.USB_PRODUCT
        )
        
        print("USB device configured")
        return True
    except Exception as e:
        print(f"Error configuring USB: {e}")
        return False

def setup_wifi():
    """Set up WiFi if enabled"""
    if not config.WIFI_ENABLED:
        print("WiFi functionality disabled")
        return False
    
    try:
        import network
        
        # Connect to WiFi
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        
        if not wlan.isconnected():
            print(f"Connecting to WiFi network: {config.WIFI_SSID}")
            wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
            
            # Wait for connection with timeout
            max_wait = 10
            while max_wait > 0:
                if wlan.isconnected():
                    break
                max_wait -= 1
                print("Waiting for WiFi connection...")
                time.sleep(1)
        
        if wlan.isconnected():
            print(f"Connected to WiFi. IP: {wlan.ifconfig()[0]}")
            return True
        else:
            print("Failed to connect to WiFi")
            return False
    
    except Exception as e:
        print(f"Error setting up WiFi: {e}")
        return False

def setup_bluetooth():
    """Set up Bluetooth if enabled"""
    if not config.BT_ENABLED:
        print("Bluetooth functionality disabled")
        return False
    
    try:
        import bluetooth
        
        # Initialize Bluetooth
        bt = bluetooth.BLE()
        bt.active(True)
        bt.config(gap_name=config.BT_NAME)
        
        print(f"Bluetooth initialized with name: {config.BT_NAME}")
        return True
    
    except Exception as e:
        print(f"Error setting up Bluetooth: {e}")
        return False

# Main boot sequence
print("\n--- ESP32 Button Box Boot Sequence ---")
print(f"MicroPython Version: {sys.version}")
print(f"Device: ESP32-WROOM-32")

# Set CPU frequency to maximum for best performance
try:
    machine.freq(240000000)  # 240 MHz
    print(f"CPU Frequency: {machine.freq() / 1000000} MHz")
except:
    print("Could not set CPU frequency")

# Set up USB if enabled
if config.USB_ENABLED:
    usb_success = setup_usb()
    print(f"USB Setup: {'Success' if usb_success else 'Failed'}")

# Set up WiFi if enabled
if config.WIFI_ENABLED:
    wifi_success = setup_wifi()
    print(f"WiFi Setup: {'Success' if wifi_success else 'Failed'}")

# Set up Bluetooth if enabled
if config.BT_ENABLED:
    bt_success = setup_bluetooth()
    print(f"Bluetooth Setup: {'Success' if bt_success else 'Failed'}")

print("Boot sequence completed")
print("-----------------------------------\n")

# Garbage collection to free up memory
import gc
gc.collect()
