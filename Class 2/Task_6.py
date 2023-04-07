my_list = input("Введите слова через пробел: ").split()
n = 1
for elem in my_list:
    if len(elem) > 10:
        print(f"{n}. {elem[:10]}")
    else:
        print(f"{n}. {elem}")
        n += 1
