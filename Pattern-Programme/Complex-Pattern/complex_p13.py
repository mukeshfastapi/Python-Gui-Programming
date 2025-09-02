# Pattern with fixed digit in every row

n = int(input("Enter nimber of rows:"))

# for i in range(n):
#     print((str(i+1)+' ')*(i+1))

for i in range(n):
    for j in range(i+1):
        print(i+1, end=" ")
    print()