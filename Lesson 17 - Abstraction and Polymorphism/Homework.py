class BMW():
    def origin(self):
        print("The BMW originated in Munich, Bavaria, Germany.")
    def creator(self):
        print("The BMW was created by Franz Josef Popp and Camillo Castiglioni.")
class Ferrari():
    def origin(self):
        print("The Ferrari originated in Maranello, Italy.")
    def creator(self):
        print("The Ferrari wass created by Enzo Ferrari.")
obj_bmw = BMW()
obj_ferrari = Ferrari()

for car in (obj_bmw, obj_ferrari):
    car.origin()
    car.creator()