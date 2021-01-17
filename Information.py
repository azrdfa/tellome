from djitellopy import Tello

tello = Tello()
tello.connect()
print("Battery Percentage:", str(tello.get_battery()), "%")
print("Drone Height:", str(tello.get_height()), "cm")
print("Drone Temperature:", str(tello.get_temperature()), "celcius")
print("Drone Yaw:", str(tello.get_yaw()), "degree")