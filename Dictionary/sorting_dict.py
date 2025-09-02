# Sorting the dict keys

# Method -1 using of sorted()

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

print('Sorting a dict by key.....')
# Sort by key
print(dict(sorted(people.items())))

print('Sorting a dict by value.....')
# Sort by value

print(dict(sorted(people.items(), key= lambda items:items[1])))

# lambda func is nothing but a callback function
