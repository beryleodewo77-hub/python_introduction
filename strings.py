# int , float , string

name = "Hunter lee"
print(name)
print(type(name)) # this here checks the type of data we are using

f_name = "Annah"
l_name = " Tom"

full_name =  f_name + l_name
# print(full_name)

print(full_name.upper())

full_upper = full_name.upper() # this means that anytime 'i' print the full name  it is going to be in uppercase
print(full_upper)

print("Jack jill".capitalize()) # makes only the first name start with a capital
print("jully jonhson".title())  # makes both names start with a capital letter

age = "12"
print(age.isnumeric()) # this checks if the data stored is containing numerical numbers if yes
                        # then it returns true.
