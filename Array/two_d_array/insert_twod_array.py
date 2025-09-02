# insert elements two d array
import numpy as np

twoDArray = np.array([[1,2,3,4], [10,11,12,13], [21,22,23,24], [31,32,33,34]])

newTwoDArray = np.insert(twoDArray,0, [41,42,43,44], axis=0)
print(twoDArray)
print('-----------------------')
print(newTwoDArray)

newTwoDArray1 = np.insert(twoDArray,3,[51,52,53,54], axis=0)

print('-----------------------')
print(newTwoDArray1)