# accessing elements of two d array
import numpy as np

twoDArray = np.array([[1,2,3,4], [10,11,12,13], [21,22,23,24], [31,32,33,34]])
print(twoDArray)

def access(array, rowindex, colindex):
    if rowindex >= len(array) or colindex >= len(array):
        print('Index out of range...')
    else:
        print(array[rowindex][colindex])

access(twoDArray,1,2)
print()

access(twoDArray, 3,3)
print()
access(twoDArray,12,3)