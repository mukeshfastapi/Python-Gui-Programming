# Searching an element from the two D array
import numpy as np

twoDArray = np.array([[1,2,3,4], [10,11,12,13], [21,22,23,24], [31,32,33,34]])

print(twoDArray)

print('-----------------')

def searching(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return 'The value is located at' +str (i) + ' ' + str (j)
    return 'The Element not found'

print(searching(twoDArray, 22))
print(searching(twoDArray, 100))
