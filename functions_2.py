from arrays import people


def add(a, b, c):  # this just add 3 parameters abc
    result = a + b + c
    return result


def addition(*nums):  # this accepts addition of one or many nums
    # how to put a documentation that when someone hovers over they see.
    """
    adds any number of numbers
    parameter:
      integers, floats, or a mix of integers and floats
    returns:
      integers or floats
    """
    total = sum(nums)
    return total
addition(3,3,4)

def build_profile(**kwargs):  # dictionary key/word arguments
    for k, w in kwargs.items():
        print(f"{k} : {w}  ")


def fancy_function(x, *nums, **kwargs):# this combines everything
    print(x)
    print(nums)
    print(kwargs)

# call function

# print(add(2,3,4))
# print(addition(9, 7, 5,8,9,10))
# print(addition(1,4,5,6,))
# print(addition(1,2,3,4,5,6,7,8,9))

# build_profile(experience = 100, name = "Jane Mary", age = "24", profession = "Engineering")

# anonymous = lambda functions do not have names.
# def square(num):
#     return num ** 2 # num * num

# result = square(3)
# print(result)

square = lambda num: num * num # this is a lambda func

print(square(5))
result = square(5.5)
print(result)


surface_area_cylinder = lambda r,h : 22/7 * r**2 * 2 + 22/7 * 2 * r * h
print(surface_area_cylinder(7,20))


people = [
    {"name": "Dora","age": 22 },
    {"name": "Bob", "age": 24 },
    {"name": "Danny", "age": 25 },
    {"name": "Kira", "age": 26 },
    {"name": "Tyra", "age": 27 },
]
sorted_by_age = sorted(people, key=lambda x: x["age"] , reverse=True)
print(sorted_by_age)
