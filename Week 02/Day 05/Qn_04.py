# Create a subclass of `Truck` called `HybridTruck`. Add an additional attribute:
#    - `electric_motor_power`: Power of the electric motor in the hybrid truck
# Define the Vehicle class
class Vehicle:
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

# Define the Truck class
class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_type, payload_capacity):
        super().__init__(make, model, year, fuel_type)
        self.payload_capacity = payload_capacity

# Define the HybridTruck class
class HybridTruck(Truck):
    def __init__(self, make, model, year, fuel_type, payload_capacity, electric_motor_power):
        super().__init__(make, model, year, fuel_type, payload_capacity)
        self.electric_motor_power = electric_motor_power

# Example usage:
hybrid_truck_instance = HybridTruck(make="Volvo", model="HybridTruck", year=2022, fuel_type="Hybrid", payload_capacity=3000, electric_motor_power=150)

# Accessing attributes of HybridTruck instance
print("HybridTruck Attributes:")
print(f"Make: {hybrid_truck_instance.make}")
print(f"Model: {hybrid_truck_instance.model}")
print(f"Year: {hybrid_truck_instance.year}")
print(f"Fuel Type: {hybrid_truck_instance.fuel_type}")
print(f"Payload Capacity: {hybrid_truck_instance.payload_capacity} lbs")
print(f"Electric Motor Power: {hybrid_truck_instance.electric_motor_power} kW")
