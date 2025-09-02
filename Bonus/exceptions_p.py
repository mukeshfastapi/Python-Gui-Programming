# Try and catch implementations

try:
    width = float(input("Enter rectangle width:"))
    length = float(input("Enter rectangle width:"))

    if width == length:
        exit("Thats looks like a square:")

    area = width * length
    print(area)
except ValueError:
    print("Please Enter a Number:::")