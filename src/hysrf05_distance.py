# HYSRF05

import RPi.GPIO as GPIO
import time

class HYSRF05:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        # Set up GPIO pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def measure_distance(self):
        # Send trigger pulse
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        # Wait for echo to start
        start_time = time.time()
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        # Wait for echo to end
        end_time = time.time()
        while GPIO.input(self.echo_pin) == 1:
            end_time = time.time()

        # Calculate distance in mm
        duration = end_time - start_time
        distance_mm = duration * 17150
        return distance_mm

    def __del__(self):
        GPIO.cleanup()
