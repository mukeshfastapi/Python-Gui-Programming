# More testing about python sorting in dict

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

print(sorted(people))

# Items()
print(people.items())

# The .items() method returns a read-only dictionary view object, which serves as a window
# into the dictionary.This view is not a copy or a list—it’s a read-only iterable that’s
# actually linked to the dictionary
# it was generated from:
print()
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

view = people.items()

people[2] = 'David'

print(view)
