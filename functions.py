# functions or methods to do different things


# print("Hello World") #built in

with open("temp.txt" , "w") as file:
    file.write("99.34\n")
    file.write("100.34\n")
    file.write("54.34\n")

with open("temp.txt" , "r") as file:
    content = file.read()
    print(content)
