class NotAllNumbersException(Exception):
    def __init__(self, message="Список должен содержать только числа"):
        self.message = message
        super().__init__(self.message)
  numbers = []

while True:
    try:
        number = input("Введите число или 'stop' для выхода: ")
        if number == 'stop':
            break
        if not number.isdigit():
            raise NotAllNumbersException
        numbers.append(int(number))
    except NotAllNumbersException as e:
        print(e)
    except Exception as e:
        print("Произошла ошибка:", e)

print("Вы ввели следующие числа:", numbers)