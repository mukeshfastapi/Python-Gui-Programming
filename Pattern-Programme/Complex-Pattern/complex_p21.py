# Right angle triangle with fixed alphabet in every row

n = int(input("Enter Number Of rows:"))
for i in range(n):
    print((chr(65+i)+" ")*(n-i))