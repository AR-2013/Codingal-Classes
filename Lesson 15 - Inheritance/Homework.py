class Vehicle:
    def __init__(self, seating_max):
        self.seating_max = seating_max

    def fare(self):
        return self.seating_max * 100


class Bus(Vehicle):
    def fare(self):

        base_fare = super().fare()

        maintenance = base_fare * 0.10
        return base_fare + maintenance
    
bus = Bus(50)

print("Total Bus Fare: INR", bus.fare())
