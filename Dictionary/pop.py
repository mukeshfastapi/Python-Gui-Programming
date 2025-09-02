# using the pop() and popitems() to remove items from the dict
Dict = {"Roll_No": '16/001', "Name": 'David', 'Course': 'Python'}

print('Name is :', Dict.pop('Name'))
print()

print("Dictionary after popping Name is:", Dict)
print()

print('Mark is:', Dict.pop('Mark', -1))
print()
print("Dictionary after popping Mark:", Dict)

print("Randomly popping items:", Dict.popitem())
print('After popping item:', Dict)

print()
print("If some item not present in Dictionary:", Dict.pop('Mukesh'))
