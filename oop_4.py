# Inheritance

class Employee:
    def __init__(self, name:str, email:str, department:str, salary:float):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary

    def show_details(self):
        print(self.name)
        print(self.department)
        print(self.salary)

class PermanentEmployee(Employee):# inheriting
    def __init__(self, name:str, email:str, department:str, salary:float,cover, increment):
        super().__init__(name,email,department,salary)
        self.cover = cover
        self.increment = increment

class ContractEmployee(Employee):
    def __init__(self, name:str, email:str, department:str, salary:float,tenure):
        super().__init__(name,email,department,salary)
        self.tenure= tenure

p1 = PermanentEmployee("Jane Mark","jm@gmail.as","HR",89000.00,"Britam",30000)
c1 = ContractEmployee("Jin Hound","jh@gmail.vom","HR",90000.00,3)
p1.show_details()
c1.show_details()

# TODO overriding
#oop python on YouTube tutorials