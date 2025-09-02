# inverted right angle triangle with digits ascending order

n = int(input("Enter Number of rows:"))

for i in range(n):
    for j in range(n-i):
        print(j+1, end=" ")
    print()