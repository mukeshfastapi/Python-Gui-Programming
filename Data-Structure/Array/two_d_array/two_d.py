import  array as arr

ar = [[1,2,3],[4,5,6],[7,8,9]]

for r in ar:
    for c in r:
        print(c, end= " ")
    print()

# Inserting elements in two d array
ar.insert(1, [22, 33, 44])
print('after inserting the elements')
print()
for r in ar:
    for c in r:
        print(c, end= " ")
    print()

# Appending elements in two d array
print('after Appending the elements')
print()
ar.append([100, 101, 1021, 200])

for r in ar:
    for c in r:
        print(c, end= " ")
    print()

# Deleting

print('after Deleting the elements')
print()
del ar[1]

for r in ar:
    for c in r:
        print(c, end= " ")
    print()