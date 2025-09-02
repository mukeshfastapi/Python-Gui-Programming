# Pattern programme with alphabets reverse order
n = int(input("Enter number of rows:"))

for i in range(n):
    print((chr(64+n-i)+' ')*n)