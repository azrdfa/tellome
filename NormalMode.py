import module.keypress as kp
from djitellopy import Tello
from time import sleep

kp.init()

tello = Tello()
tello.connect()

SPEED = 50
YAW_SPEED = 150
is_flying = False

def get_input():
    left_right, front_back, up_down, yaw = 0, 0, 0, 0

    if kp.get_key("RIGHT"): left_right = SPEED
    if kp.get_key("LEFT"): left_right = -SPEED

    if kp.get_key("UP"): front_back = SPEED
    if kp.get_key("DOWN"): front_back = -SPEED

    if kp.get_key("w"): up_down = SPEED
    if kp.get_key("s"): up_down = -SPEED

    if kp.get_key("a"): yaw = -YAW_SPEED
    if kp.get_key("d"): yaw = YAW_SPEED

    return [left_right, front_back, up_down, yaw]

while True:
    if not is_flying:
        if kp.get_key("RETURN"): 
            tello.takeoff()
            is_flying = True
    else:
        if kp.get_key("ESCAPE"):
            tello.land()
            is_flying = False
        else:
            velocity = get_input()
            tello.send_rc_control(velocity[0], velocity[1], velocity[2], velocity[3])
    sleep(0.05)

