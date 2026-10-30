# bank acc == owner,acc number , balance , history
from datetime import date, datetime
from http import client


class Client:
    def __init__(self, name:str, kra_pin:str, dob:str, gender:str):
        self.name = name
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    def print_detail(self):
        print(self.name)
        print(self.kra_pin)

    def calc_age(self):  # pass tells the code to wait for a while if you don't have content yet = date.today()
       today = date.today()
       birth_date = datetime.strptime(self.dob, '%Y-%m-%d')
       age = today.year - birth_date.year
       return age


class BankAccount(Client):
    def __init__(self, owner:Client, acc_no:str, balance:int):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += abs(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")

        else:
            self.balance -= abs(amount)

    def print_detail(self):
        # print(self.owner.name)
        self.owner.print_detail()
        print(self.acc_no)
        print(self.balance)
        print("---------------------")


Joseph = Client('Joseph kim', 'A0021', '1999-01-12', 'M')
Jane = Client('Jane mang', 'A0021', '1997-01-12', 'F')

acc1 = BankAccount(Jane, '0928828922', 80_000)
acc2 = BankAccount(Jane, '0928828922', 70_000)
acc3 = BankAccount(Joseph, '0928828922', 80_000_000)

acc1.deposit(100_000)
acc1.deposit(10_000)

acc1.print_detail()
acc1.withdraw(100)
acc1.print_detail()

print("Jane's Age" ,Jane.calc_age())
print("Joseph's Age" ,Joseph.calc_age())

# print(acc1.owner. name. acc1.owner.calc_age()) wrong call
print(Jane.name, Jane.calc_age())



# dob = '22-04-2003'  # d/m/Y 'y' is caps because it is 4 digit/ time = hh:mm:ss
#
# today = date.today()
# # print(f"{today.day}-{today.month}-{today.year}")
#
# # convert str to date
# birth_date = datetime.strptime(dob, '%d-%m-%Y')
#
# age = today.year - birth_date.year
# print(age)
