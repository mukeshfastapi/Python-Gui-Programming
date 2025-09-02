# Inverted right angle triangle with fixed alphabet symbol
n = int(input("Enter Number of rows:"))

for i in range(n):
    print((chr(64+n-i)+ " ") * (n-i))