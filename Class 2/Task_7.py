my_list = [7, 5, 3, 3, 2]
while True:
    n = input("Введите оценку от 1 до 10 'q' для выхода: " )
    if n != 'q':
        my_list.append(int(n))
        print(my_list)
    else:
        break
