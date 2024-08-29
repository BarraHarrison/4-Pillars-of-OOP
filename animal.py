# Tools for OOP

# 4 Pillars of OOP
# Abstraction, Inheritance, Polymorphism and Encapsulation

# Abstraction
class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        return "Some generic noise!"

    def eat_food(self):
        return "Eating food!"

# Inheritance
# Dog and Bird are children of the main Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_noise(self):
        return "Woof!"

class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def make_noise(self):
        return "Chirp!"

# Polymorphism (demonstrated by the make_noise method)
def main():
    dog_variable = Dog("Buddy", "German Shepherd")
    bird_variable = Bird("Polly", "Parrot")

    print(f"{dog_variable.name}, a {dog_variable.breed}, says: {dog_variable.make_noise()}")
    print(f"{bird_variable.name}, a {bird_variable.species}, says: {bird_variable.make_noise()}")

    # Demonstrating encapsulation by calling eat_food() from the parent class
    print(f"{dog_variable.name} is {dog_variable.eat_food()}")
    print(f"{bird_variable.name} is {bird_variable.eat_food()}")

if __name__ == "__main__":
    main()
