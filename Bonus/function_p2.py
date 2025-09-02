# Decoupling functions find meters

feet_inches = input("Enter feet and inches:")

def convert_meters(feet_inches):
    part = feet_inches.split()
    feet = float(part[0])
    inches = float(part[1])
    meters = feet * 0.3048 + inches * 0.254
    return meters

result = convert_meters(feet_inches)


if result < 1:
    print('Kid is too small')
else:
    print('Kid can use slide')