class Parrot():
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

bloo = Parrot("Bloo", 12)
woo = Parrot("Woo", 14)

print("Bloo is a", bloo.species)
print("Woo is a", woo.species)

print("{} is {} years old.".format(bloo.name, bloo.age))
print("{} is {} years old.".format(woo.name, woo.age))