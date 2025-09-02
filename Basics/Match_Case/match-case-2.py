# Checking even odd number using match case

def num_check(x):
    match x:
        case x if x % 2 == 0:
            print('Even number')

        case _:
            print('Odd Number')

num_check(10)

print()

num_check(15)