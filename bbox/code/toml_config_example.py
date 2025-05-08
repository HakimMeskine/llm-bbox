# ESP32 Button Box - TOML Configuration Example
# This file demonstrates how to load and use the TOML configuration file

import tomli  # For Python 3.11+, use 'tomllib' from the standard library instead

def load_config(config_path="../config.toml"):
    """
    Load configuration from a TOML file
    
    Args:
        config_path: Path to the TOML configuration file
        
    Returns:
        dict: Configuration dictionary
    """
    try:
        with open(config_path, "rb") as f:
            config = tomli.load(f)
        return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return None

def print_config_summary(config):
    """
    Print a summary of the loaded configuration
    
    Args:
        config: Configuration dictionary
    """
    if not config:
        print("No configuration loaded")
        return
    
    print("\n=== ESP32 Button Box Configuration ===\n")
    
    # Project info
    print(f"Project: {config['project']['name']} v{config['project']['version']}")
    print(f"Description: {config['project']['description']}")
    print()
    
    # Hardware configuration
    print("=== Hardware Configuration ===")
    print(f"Button Matrix: {len(config['hardware']['button_matrix']['row_pins'])}x{len(config['hardware']['button_matrix']['col_pins'])} grid")
    print(f"Row Pins: {config['hardware']['button_matrix']['row_pins']}")
    print(f"Column Pins: {config['hardware']['button_matrix']['col_pins']}")
    print(f"Rotary Encoders: 2")
    print(f"Funky Switch: 7-way with push button")
    print(f"Status LEDs: 2")
    print()
    
    # Interface configuration
    print("=== Interface Configuration ===")
    print(f"USB HID: {'Enabled' if config['interface']['usb']['enabled'] else 'Disabled'}")
    print(f"WiFi: {'Enabled' if config['interface']['wifi']['enabled'] else 'Disabled'}")
    print(f"Bluetooth: {'Enabled' if config['interface']['bluetooth']['enabled'] else 'Disabled'}")
    print()
    
    # Performance settings
    print("=== Performance Settings ===")
    print(f"Button Debounce Time: {config['performance']['debounce_time_ms']} ms")
    print(f"Encoder Debounce Time: {config['performance']['encoder_debounce_ms']} ms")
    print(f"Matrix Scan Interval: {config['performance']['matrix_scan_interval_ms']} ms")
    print(f"Encoder Scan Interval: {config['performance']['encoder_scan_interval_ms']} ms")
    print()

def get_pin_config(config):
    """
    Extract pin configuration from the loaded config
    
    Args:
        config: Configuration dictionary
        
    Returns:
        dict: Pin configuration dictionary
    """
    pins = {}
    
    # Button matrix pins
    pins['row_pins'] = config['hardware']['button_matrix']['row_pins']
    pins['col_pins'] = config['hardware']['button_matrix']['col_pins']
    
    # Rotary encoder pins
    pins['encoder1'] = {
        'clk': config['hardware']['rotary_encoders']['encoder1_clk_pin'],
        'dt': config['hardware']['rotary_encoders']['encoder1_dt_pin'],
        'sw': config['hardware']['rotary_encoders']['encoder1_sw_pin']
    }
    
    pins['encoder2'] = {
        'clk': config['hardware']['rotary_encoders']['encoder2_clk_pin'],
        'dt': config['hardware']['rotary_encoders']['encoder2_dt_pin'],
        'sw': config['hardware']['rotary_encoders']['encoder2_sw_pin']
    }
    
    # Funky switch pins
    pins['funky_switch'] = {
        'up': config['hardware']['funky_switch']['up_pin'],
        'down': config['hardware']['funky_switch']['down_pin'],
        'left': config['hardware']['funky_switch']['left_pin'],
        'right': config['hardware']['funky_switch']['right_pin'],
        'up_left': config['hardware']['funky_switch']['up_left_pin'],
        'up_right': config['hardware']['funky_switch']['up_right_pin'],
        'down_left': config['hardware']['funky_switch']['down_left_pin'],
        'down_right': config['hardware']['funky_switch']['down_right_pin'],
        'sw': config['hardware']['funky_switch']['sw_pin']
    }
    
    # Status LED pins
    pins['status_leds'] = {
        'led1': config['hardware']['status_leds']['led1_pin'],
        'led2': config['hardware']['status_leds']['led2_pin']
    }
    
    return pins

def main():
    """
    Main function to demonstrate loading and using the TOML configuration
    """
    # Load configuration
    config = load_config()
    
    if not config:
        print("Failed to load configuration. Exiting.")
        return
    
    # Print configuration summary
    print_config_summary(config)
    
    # Example: Get pin configuration
    pins = get_pin_config(config)
    
    # Example: Use the configuration in your application
    print("=== Example: Using Configuration ===")
    print(f"Setting up button matrix with {len(pins['row_pins'])} rows and {len(pins['col_pins'])} columns")
    print(f"Configuring rotary encoder 1 on pins CLK={pins['encoder1']['clk']}, DT={pins['encoder1']['dt']}, SW={pins['encoder1']['sw']}")
    print(f"USB HID {'enabled' if config['interface']['usb']['enabled'] else 'disabled'} with VID={config['interface']['usb']['vendor_id']}, PID={config['interface']['usb']['product_id']}")

if __name__ == "__main__":
    main()
