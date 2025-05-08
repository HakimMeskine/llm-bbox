# ESP32 Button Box TOML Configuration

This document explains the TOML configuration file for the ESP32 Button Box project.

## Overview

The project now includes a TOML (Tom's Obvious, Minimal Language) configuration file that provides a more structured and maintainable way to configure the button box. TOML is a configuration file format that's designed to be easy to read and write, with a simple structure.

The configuration file (`config.toml`) contains all the settings previously found in `code/config.py`, but in a more organized format that's easier to modify without having to edit Python code directly.

## Benefits of Using TOML

- **Separation of Configuration and Code**: Keeps configuration separate from implementation
- **Human-Readable**: Easy to understand and modify without programming knowledge
- **Structured Format**: Organizes related settings into sections
- **Comments Support**: Allows for documentation within the configuration file
- **Standard Format**: Widely used configuration format with good tooling support

## File Structure

The TOML configuration file is organized into several sections:

- **[project]**: Basic project information
- **[hardware]**: Hardware-related configuration
  - **[hardware.button_matrix]**: Button matrix configuration
  - **[hardware.rotary_encoders]**: Rotary encoder configuration
  - **[hardware.funky_switch]**: Funky switch configuration
  - **[hardware.status_leds]**: Status LED configuration
- **[interface]**: Interface-related configuration
  - **[interface.usb]**: USB HID configuration
  - **[interface.wifi]**: WiFi configuration
  - **[interface.bluetooth]**: Bluetooth configuration
- **[performance]**: Performance-related settings
- **[build]**: Build configuration
- **[tools]**: Tools configuration

## Using the Configuration

To use the TOML configuration in your Python code, you'll need to:

1. Install the `tomli` package (for Python < 3.11) or use the built-in `tomllib` (for Python >= 3.11)
2. Load the configuration file
3. Access the configuration values

### Example Code

```python
# For Python < 3.11
import tomli

# For Python >= 3.11
# import tomllib as tomli

def load_config(config_path="config.toml"):
    with open(config_path, "rb") as f:
        return tomli.load(f)

# Load the configuration
config = load_config()

# Access configuration values
row_pins = config["hardware"]["button_matrix"]["row_pins"]
usb_enabled = config["interface"]["usb"]["enabled"]
```

See the `code/toml_config_example.py` file for a complete example of how to load and use the TOML configuration.

## Modifying the Configuration

To modify the configuration:

1. Open the `config.toml` file in any text editor
2. Make your changes, following the TOML syntax
3. Save the file
4. Restart your application to apply the changes

## TOML Syntax Reference

Here's a quick reference for TOML syntax:

- **Comments**: Start with `#`
- **Key-Value Pairs**: `key = value`
- **Sections**: `[section]` or `[section.subsection]`
- **Arrays**: `array = [1, 2, 3]` or multi-line arrays:
  ```toml
  array = [
    1,
    2,
    3
  ]
  ```
- **Strings**: `string = "value"` (use double quotes)
- **Numbers**: `integer = 42`, `float = 3.14`
- **Booleans**: `enabled = true`, `disabled = false`

For more details on TOML syntax, see the [official TOML documentation](https://toml.io/).

## Migration from config.py

If you've been using the `config.py` file for configuration, you can migrate to the TOML configuration by:

1. Ensuring all your configuration values are present in the `config.toml` file
2. Updating your code to load configuration from the TOML file instead of importing from `config.py`
3. Using the loaded configuration dictionary to access your settings

The `toml_config_example.py` file provides a starting point for this migration.

## Dependencies

To use the TOML configuration with MicroPython on the ESP32, you'll need to:

1. Install the `micropython-tomli` package on your development machine
2. Copy the `tomli.py` file to your ESP32 along with your application code

For regular Python environments, install the `tomli` package:

```
pip install tomli
```

For Python 3.11+, the `tomllib` module is included in the standard library, so no additional installation is needed.
