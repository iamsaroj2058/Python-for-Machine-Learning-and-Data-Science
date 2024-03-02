""" Create a base class called `Vehicle` with the following attributes:
   - `make`: Make of the vehicle (e.g., Ford, Honda).
   - `model`: Model of the vehicle (e.g., Civic, F-150).
   - `year`: Year of manufacture.
   - `fuel_type`: Type of fuel the vehicle uses (e.g., Gasoline, Electric)."""
class Vehicle:
    def __init__(self, make, model, year, fuel_type):
        """
        Initialize a Vehicle with make, model, year, and fuel_type.
        """
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

# Example usage:
car = Vehicle(make="Ford", model="F-150", year=2022, fuel_type="Gasoline")

# Accessing attributes of the Vehicle
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Year: {car.year}")
print(f"Fuel Type: {car.fuel_type}")
