# Inserting elements two d array on column
import numpy as np

twoDArray = np.array([[1,2,3,4], [10,11,12,13], [21,22,23,24], [31,32,33,34]])

newTwoDArray = np.insert(twoDArray,0, [41,42,43,44], axis=1)
print(twoDArray)
print('-----------------------------------')
print()
print(newTwoDArray)
newTwoDArray1 =np.insert(newTwoDArray,2, [61,62,63,64], axis=1)
print('-----------------------------------')
print()
print(newTwoDArray1)