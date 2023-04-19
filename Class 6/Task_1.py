import time

class TrafficLight:
    def __init__(self):
        self.__color = "Red"

    def running(self):
        while True:
            print("Traffic light is on " + self.__color)
            if self.__color == "Red":
                time.sleep(7)
                self.__color = "Yellow"
            elif self.__color == "Yellow":
                time.sleep(2)
                self.__color = "Green"
            elif self.__color == "Green":
                time.sleep(5)
                self.__color = "Red"
traffic_light = TrafficLight()
traffic_light.running()
