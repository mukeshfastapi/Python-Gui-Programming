# Triangle programme alphabets descending order

n = int(input("Enter Number of rows:"))
for i in range(n):
    for j in range(i+1):
        print(chr(64+n-j), end=" ")
    print()