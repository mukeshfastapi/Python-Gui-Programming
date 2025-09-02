# Pattern programme for alphabets reverse order
n = int(input("Enter number of rows:"))
for i in range(n):
    for j in range(n):
        print(chr(64+n-j), end=' ')
    print()