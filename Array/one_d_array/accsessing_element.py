# Accessing Element of an array
from array import *

arr = array('i', [1, 2, 3, 4, 5, 56])

# access through function
def access(index, ar):
    if index >= len(ar):
        print('Array length out of range ')

    else:
        print(array[index])

access(1, arr)
access(5, arr)
access(10, arr)
