# motor_store.py

class MotorStore:
    def __init__(self):
        self.store = {}

    def get_angle(self, channel):
        if channel in self.store:
            return self.store[channel]
        else:
            self.store[channel] = 0.0
            return 0.0

    def set_angle(self, channel, angle):
        self.store[channel] = angle
