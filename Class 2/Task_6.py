my_list = input("Bведите слова через пробел: ").split()
for a, el in enumerate(my_list, 1):
    print(f'{a}. {el[:10]}')
