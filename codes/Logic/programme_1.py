def my_fun(x):
    if x == 0:
        return 0

    else:
        return x + my_fun(x - 1)

print(my_fun(5))