class Circle:
    def __init__(self, r):
        self.radius = r

    def circle_area(self):
        pi = 3.141
        return self.radius * self.radius * pi
    
r = int(input("What is the value of the radius: "))
newCircle = Circle(r)
print(newCircle.circle_area())