my_list = input("Bведите целые числа через пробел: ").split(' ')
a, b = 0, 1
while len(my_list) > b:
    my_list[a], my_list[b] = my_list[b], my_list[a]
    a += 2
    b += 2
print('Результат', *my_list)