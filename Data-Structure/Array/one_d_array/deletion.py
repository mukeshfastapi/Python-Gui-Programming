from array import *

ar = array('i', [1,2,3,4,5,6])

ar.remove(5)
for i in range(len(ar)):
    print(ar[i])
print(ar)


