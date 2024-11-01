from DroneBlocksTelloSimulator import SimulatedDrone
import json

if __name__ == '__main__':

    #sim_key = '37a0b7a9-b1e0-4f47-9c41-c3a657503452'
    #drone = SimulatedDrone(sim_key)
    with open("config.json", "r") as f:
        config = json.load(f)
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