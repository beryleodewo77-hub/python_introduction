# object-oriented programming works with classes

class Person:
    # constructor :class contains the data
    def __init__(self, name, dob, weight, height, tone):
        self.name = name
        self.dob = dob
        self.weight = weight
        self.height = height
        self.tone = tone

#functions manipulates the class data

    def display(self):
        print(f"Name is {self.name} and dob is {self.dob}")

    def get_bmi(self):
        result = self.weight / self.height * self.height
        return round(result, 2)

# Blueprint for creating objects

p1 = Person("Hellen","08-11-2001",56.88, 169, "Black")
p2 =Person("Maris Kim","03-11-2000",46.88 ,171, "Black")
p1.display()
p2.display()

print(f"{p1.name} bmi is {p1.get_bmi()}")
print(f"{p2.name} bmi is {p2.get_bmi()}")#ctrl +d duplicates