# Updating the list in many way

int_list = [1, 2, 3, 4, 5, 6]
print('Intial list :', int_list)
int_list[2] = 33
print('Updated List :', int_list)

print()

# Update the list using insert()
int_list.insert(0, 11)
print('Updated List :', int_list)

print()

# Update the list using append()
int_list.append(66)
print('Updated List :', int_list)

print()
# Update the list using extend()
int_list.extend([10,11,12])

print('Updated List :', int_list)