# Different kind of array operations

from array import *

# 1.create an array and Traverse

arr = array('i', [1,2,3,4,5,6])

for i in arr:
    print(i)

# 2. Accessing individual elements through indexes
print('coming through step 2')
print(arr[0])

# 3. Append any value to the array using append() method
print(' step 3')

arr.append(7)
print(arr)

# 4.Insert value in an array using insert() method
print('step 4.....')
arr.insert(7, 8)
print(arr)

# 5.Extend array using extend() method
print('step 5.....')

# 6.Need to use a new array to extend the old array

arr1 = array('i', [10,11,12])
arr.extend(arr1)
print(arr)

# 7.Add items from list into array using fromlist() method
print('step 6.....')
temp_list = [20,21,22]
arr.fromlist(temp_list)
print(arr)

# 8.remove any array element using remove() method
print('step 7.....')

arr.remove(22)
print(arr)

# 9.Remove last element using pop() method
print('step 8.....')

arr.pop()
print(arr)

# 10.Fetch any elements through its index using index() method
print('step 9.....')
print(arr.index(20))

# 11.Reverse a python array using reverse() method
print('step 10.....')
print(arr.reverse())
print(arr)

# 12.Get array buffer information through buffer_info() method
print('step 11.....')
print(arr.buffer_info())

# 13.Check Number off occurances of an elements using count() method
print('step 12.....')
arr.append(1)
print(arr.count(1))

# 14.Convert array to string using tostring() method
print('step 13.....')
# my_arr = array('i', [1,2])
# strTemp = my_arr.tostring()
# print(strTemp)
# ints = array('i')
# ints.fromstring(strTemp)
# print(ints)

# 15.Convert array to a list with same elements using tolist() method
print('step 14.....')
# print(arr.tolist())

# 16.Append a string to char array using fromstring() method

# 17.Slice elements from  a array
print('step 16.....')
print(arr)
print(arr[1:4])
print(arr[2:])
print(arr[:4])
print(arr[:])










