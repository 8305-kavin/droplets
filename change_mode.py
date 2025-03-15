from pymavlink import mavutil

# Connect to the drone (Change port accordingly)
master = mavutil.mavlink_connection('COM17', baud=115200)  # Windows
# master = mavutil.mavlink_connection('/dev/ttyUSB0', baud=115200)  # Linux

# Wait for a heartbeat (Ensures connection)
master.wait_heartbeat()
print("✔ Heartbeat received. Drone is connected!")

# Function to change flight mode
def set_mode(mode):
    if mode not in master.mode_mapping():
        print(f"❌ Mode {mode} not available")
        return
    mode_id = master.mode_mapping()[mode]
    master.mav.set_mode_send(master.target_system,
                             mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
                             mode_id)
    print(f"✅ Switched to {mode}")

# Change to GUIDED mode
set_mode("GUIDED")
