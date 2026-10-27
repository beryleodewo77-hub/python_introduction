# Arrays stores many items

#         # list: start counting at position 0.
# ages = [21, 23, 45, 35, 65, 22, 36, 29]
# names = ["Zack", "Jane", " Alice", " Monah"]
# # functions
# ages.append(31)  # this adds something to the list
#
# # ages.clear() # removes everything
# ages.sort() # Arrange in ascending order
# ages.reverse() # in descending order.
# print(ages)
#
# names. sort()
# print(names)
#
# Jane_count = names.count("Jane")
# print(Jane_count)
#
#
# print(len(names))
# print(len(ages))
#
# print(sum(ages)/len(ages)) # this calculates the average
#
# #retrieve an element
#
# print(ages[1])
# print(ages[-0]) # in python '-0' starts counting from the end
# print(names[0])
# print(names[-2:]) # slicing a list use '-x:' example '-5:' will give the last five from the last
#                     #'2:' give top 2 from start
#
# print(ages[2:3]) # means it gives from index 2 but not the 3 one
# print(ages[::2]) # slice by skipping one number
# print(ages[::-1]) #
# print(ages[:2]) #


# set : mutable
scores = {88, 78, 84, 93, 90, 88, 23}  # no duplication allowed
scores.add(99)
print(scores)

# tuples are immutable cannot be modified
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(weekdays)

# Dictionary:  stores in key (string)and values
person = {"name": "John", "age": 88, "height": 78}
print(person["name"])
print(person["age"])

# List of dictionaries
people = [{"name": "Dora", "age": 88, "height": 78},
          {"name": "Jane", "age": 23, "height": 48},
          {"name": "Jilly", "age": 48, "height": 88}
          ]
print(people[0]["name"])
