class Vehicle:
    def __init__(VehicleType):
        print("This vehicle is a", VehicleType)
class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__('Car')
print(issubclass(Car, Vehicle))
print(issubclass(Car, list))
print(issubclass(Car, Car))
print(issubclass(Car, (list, Vehicle)))