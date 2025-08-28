
import random
import time
import sys
from collections import deque

# Constants for the simulation
NORMAL_HEART_RATE_MIN = 60
NORMAL_HEART_RATE_MAX = 100
ANOMALY_RATE_MIN = 130
ANOMALY_RATE_MAX = 150
BUFFER_SIZE = 10  # Number of heart rate readings to store for analysis
ALERT_THRESHOLD = 3 # Number of consecutive anomalies to trigger a full alert

# Use a deque for efficient storage and removal of readings
heart_rate_buffer = deque(maxlen=BUFFER_SIZE)

def generate_heart_rate(is_anomaly=False):
    """
    Simulates a heart rate reading.
    If is_anomaly is True, it generates an abnormally high reading.
    """
    if is_anomaly:
        return random.randint(ANOMALY_RATE_MIN, ANOMALY_RATE_MAX)
    else:
        # Simulate slight variations in a normal heart rate
        return random.randint(NORMAL_HEART_RATE_MIN, NORMAL_HEART_RATE_MAX)

def main():
    """
    Main function to run the data stream simulation and analysis in a single loop.
    """
    print("Starting single-threaded data stream simulation.")
    anomaly_count = 0
    try:
        while True:
            # Step 1: Generate a new heart rate reading
            is_anomaly_present = random.random() < 0.1 # 10% chance of an anomaly
            reading = generate_heart_rate(is_anomaly_present)
            heart_rate_buffer.append(reading)
            print(f"[{time.strftime('%H:%M:%S')}] New Reading: {reading} bpm")

            # Step 2: Analyze the latest reading and check for anomalies
            last_reading = heart_rate_buffer[-1]
            if last_reading >= ANOMALY_RATE_MIN:
                anomaly_count += 1
                print(f"*** Potential Anomaly Detected! ({anomaly_count}/{ALERT_THRESHOLD}) ***")
                # Trigger a full alert if threshold is reached
                if anomaly_count >= ALERT_THRESHOLD:
                    print("!!! ALERT: CRITICAL ANOMALY DETECTED !!!")
                    print("!!! Patient requires immediate medical attention !!!")
                    # Break the loop after a critical alert
                    break
            else:
                # Reset the count if the reading is normal
                anomaly_count = 0
            
            # Pause for 1 second before the next loop iteration
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 


