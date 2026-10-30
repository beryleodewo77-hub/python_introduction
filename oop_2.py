
class Circle:
    def __init__(self, radius:int):#setup data
        self.radius = radius

    def area(self):
        return round(22/7* self.radius**2, 2)
    def perimeter(self):
        return round(22/7* self.radius* 2, 2 )

    def print_details(self):
        print("Radius is :",self.radius)
        print("Perimeter:",self.perimeter())
        print("Area:",self.area())

c1= Circle(10)
c2= Circle(28)
c3= Circle(20)

print(c1.area())

c1.print_details()