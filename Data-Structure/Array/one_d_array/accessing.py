from array import *

ar = array('i', [1,2,3,4,5,6])

def accessElement(array, index):
    if index >= len(array):
        print('Array length out of range')
    else:
        print(array[index])

accessElement(ar, 8)

accessElement(ar, 5)