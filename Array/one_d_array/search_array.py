# Searching elements from an array through linear search

from array import *

arr = array('i', [1,2,3,4,5,56])

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

print(linear_search(arr, 5))

print(linear_search(arr, 60))