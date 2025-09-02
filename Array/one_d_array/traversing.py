# Python Programme for traversing an array
import  array as arr

ar = arr.array('i', [1,2,3,4,5,6])
ar_2 = arr.array('d', [1.3,1.2,1.5])
ar_3 = arr.array('f', [10.2, 11.3, 12.5])

# function for traversing an array

def traverse(array):
    for i in array:
        print(i)

traverse(ar)
print('---------')
traverse(ar_2)

print()
print('--------------------')
traverse(ar_3)