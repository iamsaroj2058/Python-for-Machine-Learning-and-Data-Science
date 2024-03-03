class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def animal_sound(animal):
    animal.speak()

# Creating instances of different classes
animal = Animal()
dog = Dog()
cat = Cat()

# Using the function with different objects
animal_sound(animal)  # Output: Animal speaks
animal_sound(dog)     # Output: Dog barks
animal_sound(cat)     # Output: Cat meows
