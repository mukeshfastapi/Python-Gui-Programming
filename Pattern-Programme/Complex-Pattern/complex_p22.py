# Right Angle triangle with fix digit in every row decreasing order
n = int(input("Enter number of rows:"))
for i in range(n):
    print((str(n-i) + " ")*(n-i))