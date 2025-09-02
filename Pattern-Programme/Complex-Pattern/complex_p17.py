# Pattern programme for printing digits in descending order

n = int(input("Enter number of rows:"))

for i in range(n):
    for j in range(i+1):
        print(n-j, end=" ")

    print()