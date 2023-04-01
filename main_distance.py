from src.hysrf05_distance import HYSRF05
import time

# Conectăm pinul VCC la pinul 5V al Raspberry Pi, 
# pinul GND la pinul GND al Raspberry Pi, 
# pinul Echo la pinul GPIO 18 (BCM), 
# pinul Trigger la pinul GPIO 23 (BCM)
if __name__ == "__main__":
    hysrf05 = HYSRF05(23, 18)
    try:
        while True:
            distance = hysrf05.measure_distance()
            print(f"Distance: {distance:.2f}")
            time.sleep(0.1)  # Wait for 100 milliseconds before measuring again

    except KeyboardInterrupt:
        del hysrf05
        pass
