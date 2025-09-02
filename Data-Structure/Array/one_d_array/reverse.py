import  array as arr

ar = arr.array('i', [1,2,3,4])



for i in range(len(ar)):
    print(ar[i])

print()

ar.reverse()

# print(rev)

for i in range(len(ar)):
    print(ar[i])