def divide_numbers():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a / b
        print("Результат деления: ", result)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")

divide_numbers()