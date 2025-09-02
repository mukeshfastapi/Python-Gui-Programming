# Traversing an array using  function

import numpy as np

twoDArray = np.array([[1,2,3,4], [10,11,12,13], [21,22,23,24], [31,32,33,34]])

print(twoDArray)
print('--------------')
print()

def traverse(array):
    for i in range(len(array)):   # for loop for traverse the row
        for j in range(len(array[0])):  # for loop for traverse the colomn array[0]
            print(array[i][j])

traverse(twoDArray)