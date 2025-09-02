# We should not use mutable type as key in dict
# Dict = {"Roll_No": '16/001', "Name": 'David', 'Course': 'Python', [123]: 123}

# print(Dict)

Dict_tuple = {"Roll_No": '16/001', "Name": 'David', 'Course': 'Python', (1,2,3):123}
print(Dict_tuple)

# Dict_list = {"Roll_No": '16/001', "Name": 'David', 'Course': 'Python', ([1,2,3]):123}