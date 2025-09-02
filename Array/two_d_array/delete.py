# Deleting elements from two D array
import numpy as np

twoDArray = np.array([[1,2,3,4], [10,11,12,13], [21,22,23,24], [31,32,33,34]])

print(twoDArray)

print('-----------------')

new_deleted_array = np.delete(twoDArray, 0, axis=0)
print()
print('New row deleted array')
print(new_deleted_array)

new_deleted_array1 = np.delete(twoDArray, 1, axis=1)
print()
print('New coloumn deleted array')
print(new_deleted_array1)

