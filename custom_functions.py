from numbers import area


def greet():
    print("Hello friends")


def greeting(name):
    print(f"Hello{name}")


# greet() # calling the function  == use

# greeting(" Soul babel")
# greeting(" Rhine")
# greeting(" lovely")


def volume_cylinder(radius, height):
    volume = 22 / 7 * radius ** 2 * height
    print(round(volume))


def vol_better(radius, height):
    volume = 22 / 7 * radius ** 2 * height
    return round(volume)


def volume_surface(radius, height):
    volume = 22 / 7 * radius ** 2 * height
    a = 22 / 7 * radius ** 2 * height + 22 / 7 * radius ** 2 * height
    return volume, a


# volume_cylinder(10, 50)
# result = vol_better(5, 20)
# print(result)

# with open("volumes.txt", "w") as file:
#     file.write( str(result))


volume, a = volume_surface(10, 50)
print(f"volume is: {volume}and area is: {area}")

# named parameters
v, a = volume_surface(height=20, radius=10)
print(f"volume is: {v}and area is: {a}")


def divide(a=1, b=1, should_round=False):
    res = a / b
    if should_round == True:
        return round(res, 2)
    else:
        return res


print(divide(9, 5.11, True))

print(divide(b=15 , should_round=True))
