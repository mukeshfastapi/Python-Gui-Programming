# Deleting dict item on various methods

# Method 1-- use of del keyword and clear() at a time
Dict = {"Roll_No": '16/001', "Name": 'David', 'Course': 'Python'}
print("Dict[name] =",  Dict['Name'])
print("Dict[Roll_No]=", Dict['Roll_No'])
print("Dict[Course]=", Dict['Course'])

del Dict['Course']
print('After deleting course:', Dict)
Dict.clear()
print('After using clear(), dictionary contains no items:', Dict)

del Dict  # Deleting the variable which holds the Dict in Memory

print('Dict does not exist .....')

print()
print(Dict)

