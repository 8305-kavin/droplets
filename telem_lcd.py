from dronekit import connect
from RPLCD.i2c import i2c
import time

# === Setup LCD (Make sure address is correct) ===
lcd = i2c(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2)
lcd.clear()

# === Connect to APM via USB (/dev/ttyACM0) ===
try:
    print("Connecting to APM...")
    vehicle = connect('/dev/ttyACM0', baud=115200, wait_ready=True)
    print("Connected to APM!")
    lcd.write_string("APM Connected")
    time.sleep(2)
    lcd.clear()
except Exception as e:
    print("APM Connection Failed!")
    lcd.write_string("APM Error!")
    exit()

# === Function to Display Telemetry on LCD ===
def update_lcd():
    altitude = vehicle.location.global_relative_frame.alt  # Altitude
    battery = vehicle.battery.level  # Battery %
    
    lcd.clear()
    lcd.write_string(f"Alt:{altitude:.1f}m")  # First row
    lcd.crlf()  # Move to second row
    lcd.write_string(f"Bat:{battery}%")  # Second row
    
# === Loop to Continuously Update LCD ===
while True:
    update_lcd()
    time.sleep(3)  # Update every 3 seconds
