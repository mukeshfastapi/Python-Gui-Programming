# Built in dictionary methods
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

# Find the length of dict len()
print(len(people))

# String representation of the dict str(dict)
print()
print(str(people))

# Delete all entries of the dict
people1 = people
print(people1)

print(people.clear())

print(people1)

# dict copy() method

Dict = {"Roll_No": '16/001', "Name": 'David', 'Course': 'Python'}

d = Dict.copy()
print(d)
d['Name'] = 'Mukesh'
print(d)
print(Dict)