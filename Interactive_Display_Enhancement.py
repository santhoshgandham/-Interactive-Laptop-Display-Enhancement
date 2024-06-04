import serial
import pyautogui

# Disable the pyautogui failsafe feature
pyautogui.FAILSAFE = False

# Configure the serial port
serial_port = "COM8"  # Update this with your ESP32's serial port
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)

# Define the touchpad control based on distance values
def control_touchpad(x, y):
    pyautogui.moveTo(x, y)

# Assuming max_distance is the maximum distance your sensors can measure in cm (e.g., 100 cm)
max_distance1 = 30  # Replace with your sensor's max range
max_distance2 = 19
try:
    while True:
        # Read distance values from the serial port for two sensors
        distance_data = ser.readline().decode('utf-8').strip().split(',')

        try:
            # Parse distance values
            distance_A, distance_B = map(float, distance_data)
            print(f"Received distances: A={distance_A} cm, B={distance_B} cm")

            # Get the screen dimensions dynamically
            screen_width, screen_height = pyautogui.size()

            # Convert sensor data to pixel coordinates
            cursor_x = int((max_distance1 - distance_A) / max_distance1 * screen_width)
            cursor_y = int((max_distance2 - distance_B) / max_distance2 * screen_height)

            # Perform touchpad control based on calculated position
            control_touchpad(cursor_x, cursor_y)

        except ValueError:
            print(f"Invalid distance data: {distance_data}")

except KeyboardInterrupt:
    pass
finally:
    ser.close()