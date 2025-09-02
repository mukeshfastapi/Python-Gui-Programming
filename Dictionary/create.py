# Create the dictionary

# Method --1

my_dict = dict(name = 'Mukesh', age = 28)
print(my_dict)

# Method - 2 Creating dictionary using keyword arguments

name_dict = dict(name = 'Mukesh', age = 28)
print(name_dict)

# Method - 3 Creating deep-copy of the dictionary using dict() in this way it wont affect main dict
print()
main_dict = {'a': 1, 'b': 2, 'c': 3}

dict_deep = dict(main_dict)
print(dict_deep)

# shallow copy without dict
dict_shallow = main_dict

# changing value in shallow copy will change main_dict
dict_shallow['a'] = 100
print(dict_shallow)
print()
print("After change in shallow copy, main_dict:", main_dict)

print()

# changing value in deep copy won't affect main_dict
dict_deep['b'] = 20
print("After change in deep copy, main_dict:", main_dict)

print(dict_deep)

print()
# Method -4 Creating dictionary using iterables

new_dict = dict([('name','Mukesh'), ('age', 29)], d='New dict')
print(new_dict)