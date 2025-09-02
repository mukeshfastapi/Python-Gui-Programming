# Creating one dimensional array

import array as arr

a = arr.array('i', [1,2,3])

print(a)

# Accessing array
for i in range(0, 3):
    print(a[i])

print()

# Inserting element
a.insert(1, 4)

for i in range(len(a)):
    print(a[i])

print()

# Appending value to the array
a.append(10)
for i in range(len(a)):
    print(a[i])

print()

# Removing value
a.pop()
for i in range(len(a)):
    print(a[i])
print()

# Remove using remove method
a.remove(2)
for i in range(len(a)):
    print(a[i])

print()

# Searching an element in an array
a2 = arr.array('i',[1,2,3,1,2,4])

for i in range(len(a2)):
    print(a2[i])

print()

# using index() to print index of 1st occurrence of 2
print("The index of 1st occurrence of 2 is : ", end="")

print(a2.index(2))

print()

# updating an array
a2[4] = 6
for i in range(len(a2)):
    print(a2[i])

# counting elements of the array
count = a2.count(2)
print('counting the existance of 2:', count)
