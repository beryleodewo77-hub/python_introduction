# import your module first
import math

# import functions_2 as f2

#print(functions_2.my_function(200, 23.33)) # method one call  it the way it is
#f2.my_function(100,23.33) # method 2 renaming your  imported module using 'as'

# from functions_2 import my_function # method 3 imports 1 function from a particular module

# print(my_function(22,5.0))

# package is just a folder 'and' it must have a file '_init_'

from my_package import shapes

print(shapes.triangle_area(3,4,5))

print(dir(math))