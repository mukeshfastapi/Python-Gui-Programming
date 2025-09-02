# Pattern programme for alphabets dictionary order

n = int(input("Enter number of rows:"))

for i in range(n):
    for j in range(n):
        print(chr(65+j), end=" ")

    print()
