class Dog():
    breed = "dog"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

Teddy = Dog("Teddy", 1, "Golden Retriever")
Caramel = Dog("Caramel", 3, "Pomeranian")

print("Teddy is a", Teddy.breed)
print("Caramel is a", Caramel.breed)

print("{} is {} years old.".format(Teddy.name, Teddy.age))
print("{} is {} years old.".format(Caramel.name, Caramel.age))