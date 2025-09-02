class Car:
    accel = 3.0
    mpg = 25

my_car = Car()
yr_car = Car()

print('my_car accel:',my_car.accel )
print('yr_car accel:',yr_car.accel )

my_car.accel = 5.0
print()
print('my_car accel:',my_car.accel )
print('yr_car accel:',yr_car.accel )
