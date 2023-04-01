import time
from src.buttons_pcf8591 import PCF8591
from src.servo_pca9685 import MotorController

if __name__ == "__main__":
    _channel = 3
    _speed = 50

    # Use I2C bus 1
    motor = MotorController(speed=_speed, channel=_channel)

    # motor.setToOrigin()
    # time.sleep(3)
    # motor.setToHalfAngle()
    # time.sleep(3)
    # motor.setToMaxAngle()

    pcf8591 = PCF8591()
    try:
        while True:
            # btnRed = pcf8591.read_AIN0()
            # btnYellow = pcf8591.read_AIN1()
            # btnGreen = pcf8591.read_AIN2()
            # btnPush = pcf8591.read_AIN2()

            xCoord = pcf8591.read_AIN0()
            yCoord = pcf8591.read_AIN1()

            print(f"X: {xCoord}, Y: {yCoord}")

            # sw_state = pcf8591.read_SW()
            # if sw_state == 0:
            #     print("Button pressed")
            # else:
            #     print("Button not pressed")

            # print(f"X: {xCoord}, Y: {yCoord}, Sw-state: {sw_state}")

            # if btnRed == 1 :
            #     motor.setToOrigin()
            #     # motor.setToHalfAngle()
            #     # motor.setToMaxAngle()
            #     # motor.moveUpStep(increment=1)

            # if btnYellow == 1 :
            #     # motor.setToOrigin()
            #     motor.setToHalfAngle()
            #     # motor.setToMaxAngle()
            #     # motor.moveDownStep(increment=1)

            # if btnGreen == 0 :
            #     # motor.setToOrigin()
            #     # motor.setToHalfAngle()
            #     motor.setToMaxAngle()
            #     # motor.moveUp(increment=1)

            time.sleep(1)

    except KeyboardInterrupt:
        motor.stop()
        pass
