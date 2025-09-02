# Looping over the dict

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

# accessing only keys

for key in people:
    print(key, end= "->")
print()

# Accessing values

for val in people.values():
    print(val, end='->')

print()
# Accessing keys and values

for key, val in people.items():
    print(key, val)