# using the dictionary inbuilt function

# using of fromkeys() method

# Returns : A dictionary with keys mapped to None if no value is provided,
# else to the value provided in the field.

subjects = ['Python', 'FastApi', 'Django', 'Flask', 'DSA']

marks = dict.fromkeys(subjects, 35)

print(marks)

# get()
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

# Returns: Returns the value of the item with the specified key or the default value.

print(people.get('4','Notfound'))
print(people.get(4))

print()
# items()
# Returns: A view object that displays a list of a given dictionary’s (key, value) tuple pair.
Dict = {"Roll_No": '16/001', "Name": 'David', 'Course': 'Python'}

print(Dict.items())

# Keys()
# A view object is returned that displays all the keys.
# This view object changes according to the changes in the dictionary.

print()
print(Dict.keys())

# Popitem()
# removes the last inserted key-value pair from the dictionary and returns it as a tuple.
# A tuple containing the arbitrary key-value pair from dictionary.
# That pair is removed from dictionary.
print()
print(Dict.popitem())

# setdefault()
# Value of the key if it is in the dictionary.
# None if key is not in the dictionary and default_value is not specified.
# default_value if key is not in the dictionary and default_value is specified.

Dict.setdefault('Marks', 0)
print()
print(Dict)
# print(Dict.setdefault('Gender'))
print(Dict.setdefault('Gender', 'Not Defined'))


# Pop()
# Popping the last item of the dict
print(Dict.pop('Marks'))
print(Dict)

# Adding pairs to Dict using update()
Dict1 = {'Marks': 100, "Lang": "Any specified"}
Dict.update(Dict1)
print(Dict)

# Values()
# Returns:  A list of all the values available in a given dictionary.
# The values have been stored in a reversed manner.
print()
dictionary = {"Python": 2, "striver": 3, "Saad": 4}
print(dictionary.values())

# Find the sum of values
salary = {"Python": 200000, "striver": 30000, "Saad": 40000}

find_sum = salary.values()   # It is already returning a list so no need to convert to list
print(sum(find_sum))


