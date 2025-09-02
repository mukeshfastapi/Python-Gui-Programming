# Traversiong an array

import array as arr

ar = arr.array('i', [1,2,3,4,5,6])

def traverse(array):
    for i in array:
        print(i)

traverse(ar)