"""Create two subclasses: `Car` and `Truck`, inheriting from the `Vehicle` class. Implement the `__init__` method using `super().__init__` to initialize attributes from the parent class."""
class Vehicle:
    def __init__(self, make, model, year, fuel_type):
        """
        Initialize a Vehicle with make, model, year, and fuel_type.
        """
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, num_doors):
        """
        Initialize a Car with additional attribute num_doors.
        """
        super().__init__(make, model, year, fuel_type)
        self.num_doors = num_doors

class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_type, payload_capacity):
        """
        Initialize a Truck with additional attribute payload_capacity.
        """
        super().__init__(make, model, year, fuel_type)
        self.payload_capacity = payload_capacity

# Example usage:
car_instance = Car(make="Honda", model="Civic", year=2022, fuel_type="Gasoline", num_doors=4)
truck_instance = Truck(make="Ford", model="F-150", year=2022, fuel_type="Gasoline", payload_capacity=2000)

# Accessing attributes of Car instance
print("Car Attributes:")
print(f"Make: {car_instance.make}")
print(f"Model: {car_instance.model}")
print(f"Year: {car_instance.year}")
print(f"Fuel Type: {car_instance.fuel_type}")
print(f"Number of Doors: {car_instance.num_doors}")

# Accessing attributes of Truck instance
print("\nTruck Attributes:")
print(f"Make: {truck_instance.make}")
print(f"Model: {truck_instance.model}")
print(f"Year: {truck_instance.year}")
print(f"Fuel Type: {truck_instance.fuel_type}")
print(f"Payload Capacity: {truck_instance.payload_capacity} lbs")
