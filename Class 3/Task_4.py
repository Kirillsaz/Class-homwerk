def my_func(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / my_func(x, -y)
    elif y % 2 == 0:
        return my_func(x, y / 2) ** 2
    else:
        return x * my_func(x, y - 1)
