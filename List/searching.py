# Searching an item from the list

# Method - 1 using of in operator

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

target = 50

if target in my_list:
    print(f"{target} found in my_list")
else:
    print(f"{target} not found in my_list")

# Method -2 using linear search mechanism
print()
target = 30
def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(linear_search(my_list, target))

# def linear_search(p_list, p_target):
#     for i, value in p_list:  # It could not unpack non-iterable we need to unpack it using enumerate
#         if value == p_target:
#             return i
#     return -1
#
# print(linear_search(my_list, target))