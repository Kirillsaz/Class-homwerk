def my_func(a, b, c):
    smallest = min(a, b, c)
    if smallest == a:
        sum_two_largest = b + c
    elif smallest == b:
        sum_two_largest = a + c
    else:
        sum_two_largest = a + b
    return sum_two_largest
sum_two_largest = my_func(5, 10, 3)
print(sum_two_largest)
