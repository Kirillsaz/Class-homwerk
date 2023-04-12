from functools import reduce

even_numbers = [x for x in range(100, 1001, 2)]

print(even_numbers)

product = reduce(lambda x, y: x * y, even_numbers)


print(f"результат: {product}")
