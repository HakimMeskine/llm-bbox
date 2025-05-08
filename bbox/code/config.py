# ESP32 Button Box - Configuration File
# This file contains all pin assignments and configuration parameters

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

# USB HID Configuration
USB_ENABLED = True      # Set to False to disable USB HID functionality
USB_VENDOR_ID = 0x1234  # Example vendor ID (you should use your own)
USB_PRODUCT_ID = 0x5678 # Example product ID (you should use your own)
USB_MANUFACTURER = "Custom"
USB_PRODUCT = "ESP32 Button Box"

# Debounce Configuration
DEBOUNCE_TIME_MS = 20   # Debounce time in milliseconds for buttons
ENCODER_DEBOUNCE_MS = 5 # Debounce time for encoders

# Scan Rate Configuration
MATRIX_SCAN_INTERVAL_MS = 10  # Interval between button matrix scans
ENCODER_SCAN_INTERVAL_MS = 5  # Interval between encoder scans

# WiFi Configuration (if needed)
WIFI_SSID = ""          # WiFi network name
WIFI_PASSWORD = ""      # WiFi password
WIFI_ENABLED = False    # Set to True to enable WiFi

# Bluetooth Configuration (if needed)
BT_ENABLED = False      # Set to True to enable Bluetooth
BT_NAME = "ESP32ButtonBox"
