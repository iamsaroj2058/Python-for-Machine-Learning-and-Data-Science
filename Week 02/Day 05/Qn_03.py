# Create a subclass of `Car` called `ElectricCar`. Add an additional attribute:
#    - `battery_capacity`: Capacity of the electric car's battery in kWh.
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

class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_capacity):
        """
        Initialize an ElectricCar with additional attribute battery_capacity.
        """
        super().__init__(make, model, year, fuel_type="Electric", num_doors=num_doors)
        self.battery_capacity = battery_capacity

# Example usage:
electric_car_instance = ElectricCar(make="Tesla", model="Model S", year=2022, num_doors=4, battery_capacity=100)

# Accessing attributes of ElectricCar instance
print("ElectricCar Attributes:")
print(f"Make: {electric_car_instance.make}")
print(f"Model: {electric_car_instance.model}")
print(f"Year: {electric_car_instance.year}")
print(f"Fuel Type: {electric_car_instance.fuel_type}")
print(f"Number of Doors: {electric_car_instance.num_doors}")
print(f"Battery Capacity: {electric_car_instance.battery_capacity} kWh")
