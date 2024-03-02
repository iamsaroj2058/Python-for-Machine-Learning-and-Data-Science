class Car:
    def __init__(self, window, door, fuel):
        self.window = window
        self.door = door
        self.fuel = fuel

class Maruti(Car):
    def __init__(self, window, door, fuel, speed):
        super().__init__(window, door, fuel)
        self.speed = speed

    def travel(self, distance):
        fuel_required = distance / self.speed
        if fuel_required <= self.fuel:
            print(f"Travelling {distance} km at a speed of {self.speed} km/h.")
            print(f"Fuel consumed: {fuel_required} liters")
        else:
            print("Not enough fuel for the journey!")

if __name__ == "__main__":
    maruti_car = Maruti(window=4, door=4, fuel=30, speed=60)
    
    # Example usage
    maruti_car.travel(120)
