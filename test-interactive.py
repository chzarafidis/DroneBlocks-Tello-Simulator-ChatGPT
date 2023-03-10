from DroneBlocksTelloSimulator import SimulatedDrone
import json

with open("config.json", "r") as f: config = json.load(f)

drone = SimulatedDrone(config["DRONEBLOCKS_SIM_KEY"])
drone.set_speed(100)

distance = 40

drone.takeoff()
drone.fly_forward(distance,'cm')
drone.fly_left(distance,'cm')
drone.fly_backward(distance,'cm')
drone.fly_right(distance,'cm')
drone.flip_backward()
drone.land()