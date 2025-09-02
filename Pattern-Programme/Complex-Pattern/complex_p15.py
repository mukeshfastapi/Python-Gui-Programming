# Pattern programme for right angle triangle in digits
n = int(input("Enter number of rows:"))

for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")

    print()