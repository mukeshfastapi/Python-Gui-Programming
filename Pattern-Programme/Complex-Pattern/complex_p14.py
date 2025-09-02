# Pattern for printing alphabets in right angle triangle
n = int(input("Enter number of rows:"))
for i in range(n):
    print((chr(65+i)+" ")*(i+1))