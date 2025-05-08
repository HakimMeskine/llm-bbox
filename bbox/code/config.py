# ESP32 Button Box - Configuration File
# This file contains all pin assignments and configuration parameters
# Updated to include RGB LED support for SimHub integration

# Button Matrix Configuration
# Rows are outputs, columns are inputs with pull-up
ROW_PINS = [32, 33, 25, 26, 27]  # GPIO pins for rows
COL_PINS = [14, 12, 13, 15]      # GPIO pins for columns

# Button Matrix Layout (5x4 grid)
# This maps the button positions to logical button numbers
BUTTON_MAP = [
    [ 1,  2,  3,  4],  # Row 1
    [ 5,  6,  7,  8],  # Row 2
    [ 9, 10, 11, 12],  # Row 3
    [13, 14, 15, 16],  # Row 4
    [17, 18, 19, 20]   # Row 5
]

# Rotary Encoder 1 Configuration
ENCODER1_CLK_PIN = 4    # GPIO pin for CLK (A)
ENCODER1_DT_PIN = 16    # GPIO pin for DT (B)
ENCODER1_SW_PIN = 17    # GPIO pin for switch (push button)

# Rotary Encoder 2 Configuration
ENCODER2_CLK_PIN = 5    # GPIO pin for CLK (A)
ENCODER2_DT_PIN = 18    # GPIO pin for DT (B)
ENCODER2_SW_PIN = 19    # GPIO pin for switch (push button)

# RJXT1F 7-way Encoder (Funky Switch) Configuration
FUNKY_UP_PIN = 21       # GPIO pin for Up direction
FUNKY_DOWN_PIN = 22     # GPIO pin for Down direction
FUNKY_LEFT_PIN = 23     # GPIO pin for Left direction
FUNKY_RIGHT_PIN = 2     # GPIO pin for Right direction
FUNKY_UP_LEFT_PIN = 0   # GPIO pin for Up-Left direction
FUNKY_UP_RIGHT_PIN = 39 # GPIO pin for Up-Right direction (corrected from GPIO4)
FUNKY_DOWN_LEFT_PIN = 35 # GPIO pin for Down-Left direction
FUNKY_DOWN_RIGHT_PIN = 34 # GPIO pin for Down-Right direction
FUNKY_SW_PIN = 36       # GPIO pin for switch (push button)

# Status LED Configuration
STATUS_LED1_PIN = 10    # GPIO pin for status LED 1
STATUS_LED2_PIN = 9     # GPIO pin for status LED 2

# RGB LED Configuration
RGB_LED_PIN = 3         # GPIO pin for WS2812B data line (changed from GPIO21 to avoid conflict)
RGB_LED_COUNT = 20      # Number of RGB LEDs (one per button)
RGB_LED_BRIGHTNESS = 50 # Default brightness (0-255)
RGB_LED_ENABLED = True  # Set to False to disable RGB LEDs

# USB HID Configuration
USB_ENABLED = True      # Set to False to disable USB HID functionality
USB_VENDOR_ID = 0x1234  # Example vendor ID (you should use your own)
USB_PRODUCT_ID = 0x5678 # Example product ID (you should use your own)
USB_MANUFACTURER = "Custom"
USB_PRODUCT = "ESP32 Button Box"

# SimHub Integration
SIMHUB_ENABLED = True   # Set to False to disable SimHub integration
SIMHUB_PORT = 8888      # UDP port for SimHub communication

# Debounce Configuration
DEBOUNCE_TIME_MS = 20   # Debounce time in milliseconds for buttons
ENCODER_DEBOUNCE_MS = 5 # Debounce time for encoders

# Scan Rate Configuration
MATRIX_SCAN_INTERVAL_MS = 10  # Interval between button matrix scans
ENCODER_SCAN_INTERVAL_MS = 5  # Interval between encoder scans

# WiFi Configuration (required for SimHub integration)
WIFI_SSID = ""          # WiFi network name
WIFI_PASSWORD = ""      # WiFi password
WIFI_ENABLED = True     # Set to True to enable WiFi

# Bluetooth Configuration (if needed)
BT_ENABLED = False      # Set to True to enable Bluetooth
BT_NAME = "ESP32ButtonBox"

# RGB LED Effects
LED_EFFECTS = {
    "STATIC": 0,        # Static color
    "BREATHING": 1,     # Breathing effect
    "RAINBOW": 2,       # Rainbow effect
    "REACTIVE": 3,      # Reactive to button press
    "SIMHUB": 4         # Controlled by SimHub
}

# Default LED colors (RGB values)
DEFAULT_COLORS = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "CYAN": (0, 255, 255),
    "MAGENTA": (255, 0, 255),
    "WHITE": (255, 255, 255),
    "OFF": (0, 0, 0)
}

# Button to LED mapping
# Maps each button number to its corresponding LED index
BUTTON_LED_MAP = {
    1: 0, 2: 1, 3: 2, 4: 3,
    5: 4, 6: 5, 7: 6, 8: 7,
    9: 8, 10: 9, 11: 10, 12: 11,
    13: 12, 14: 13, 15: 14, 16: 15,
    17: 16, 18: 17, 19: 18, 20: 19
}
