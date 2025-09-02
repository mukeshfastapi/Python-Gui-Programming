import array as arr

ar = arr.array('i', [1,2,3])

print("The before array extend  : ", end =" ")

for i in range(len(ar)):
    print(ar[i], end=' ')

ar.extend([4,5,6,7])

print("\nThe array after extend :",end=" ")

for i in range(len(ar)):
    print(ar[i], end= " " )