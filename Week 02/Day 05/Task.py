class Animal:
    def __init__(self, *args):
        if len(args)==1:
            self.name
    def set_info(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def walk(self):
        print(f"{self.name} is walking.")

if __name__ == "__main__":
    cat = Animal(name="cat", species="Cat Family")
    cat.walk()
