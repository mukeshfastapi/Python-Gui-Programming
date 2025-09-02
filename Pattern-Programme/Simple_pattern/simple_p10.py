# pattern programme for print digits in descending order
n = int(input("Enter number of rows:"))

for i in range(n):
    for j in range(n):
        print(n-j, end=" ")

    print()