# Right angle triangle with fix digit in every row
n = int(input("Enter Number of rows:"))
for i in range(n):
    print((str(i+1)+" ") * (n-i))