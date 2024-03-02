class Car:
    def __init__(self, window, door, fuel):
        self.window = window
        self.door = door
        self.fuel = fuel

class Maruti(Car):
    def __init__(self, window, door, fuel, speed):
        super().__init__(window, door, fuel)
        self.speed = speed

    

    def travel(self):
        print(f"")


if __name__ == "__main__":
    

