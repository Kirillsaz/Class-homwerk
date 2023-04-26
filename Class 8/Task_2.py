class DivisionByZeroError(Exception):
    pass

try:
    dividend = int(input("Введите делимое: "))
    divisor = int(input("Введите делитель: "))
    if divisor == 0:
        raise DivisionByZeroError("Ошибка: деление на ноль!")
    result = dividend / divisor
    print("Результат деления:", result)
except ValueError:
    print("Ошибка: введено неверное значение!")
except DivisionByZeroError as e:
    print(e)
