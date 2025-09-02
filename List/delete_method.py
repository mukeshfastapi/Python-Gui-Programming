# Deleting Elements from the list

# Method -1 del keyword
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # This will delete the element at index 2 (which is '3')
print(my_list)

# Method -2 pop()
p = my_list.pop()  # Storing the popped value inside the variable to track which item has been deleted
print(p)
print(my_list)

# pop () with provide the value
my_list.pop(0)
print(my_list)

# Method -3 remove()
# The remove method is used to remove the first occurrence of a specific element from the list.
print()
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)  # This will remove the first occurrence of '3' from the list
print(my_list)

# Tricks---> To remove item from the list using slicing

print()
my_list = [1, 2, 3, 4, 5]

# Need to remove 3 from the list
print(my_list[:2])  # [1, 2]
print(my_list[3:])  # [4, 5]

# Creating a newlist to excluding the items basically adding the above two list

my_list = my_list[:2] + my_list[3:]
print(my_list)

# Method - 5 using of list comprehension

# Using for loop to traverse the list and remove item
print()
my_list = [1, 2, 3, 4, 5]

for x in my_list:
    if x != 3:
        print(x)

print()

my_update_list = [x for x in my_list if x != 3]
print(my_update_list)