# Demonstrate the usage of these classes by creating instances and displaying information about the vehicles.
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
# Create instances of the classes
vehicle_instance = Vehicle(make="Toyota", model="Camry", year=2022, fuel_type="Gasoline")
truck_instance = Truck(make="Ford", model="F-150", year=2022, fuel_type="Gasoline", payload_capacity=2000)
hybrid_truck_instance = HybridTruck(make="Volvo", model="HybridTruck", year=2022, fuel_type="Hybrid", payload_capacity=3000, electric_motor_power=150)

# Display information about the vehicles
print("Vehicle Information:")
print(f"Make: {vehicle_instance.make}")
print(f"Model: {vehicle_instance.model}")
print(f"Year: {vehicle_instance.year}")
print(f"Fuel Type: {vehicle_instance.fuel_type}")
print("\nTruck Information:")
print(f"Make: {truck_instance.make}")
print(f"Model: {truck_instance.model}")
print(f"Year: {truck_instance.year}")
print(f"Fuel Type: {truck_instance.fuel_type}")
print(f"Payload Capacity: {truck_instance.payload_capacity} lbs")
print("\nHybridTruck Information:")
print(f"Make: {hybrid_truck_instance.make}")
print(f"Model: {hybrid_truck_instance.model}")
print(f"Year: {hybrid_truck_instance.year}")
print(f"Fuel Type: {hybrid_truck_instance.fuel_type}")
print(f"Payload Capacity: {hybrid_truck_instance.payload_capacity} lbs")
print(f"Electric Motor Power: {hybrid_truck_instance.electric_motor_power} kW")
