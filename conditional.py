# conditional statements basically checks some conditions and make a decision
# variables are used to store values to be used later.
import os

# list, booleans, tuples , dictionaries and loops : look at these later.


Name = input("Enter your name:  ")

age = input("Enter your age:  ")
if  not age.isnumeric():
    print("Your age is invalid") # relay an interrupt

    os._exit(0)  #this is one way of terminating your program .
                  # first put os + enter, to import. or sys.exit()

if int(age) > 18:  # 'int' this will convert the age into an integer
    print(Name + "You are an Adult")
else:
    print(Name + "you are a child")

