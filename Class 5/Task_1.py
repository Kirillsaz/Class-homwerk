filename = input("Введите имя файла: ")
with open(filename, 'w') as file:
    while True:
        line = input("Введите строку данных: ")
        if line == "q":
            break
        file.write(line + "\n")
print("Данные записаны в файл ", filename)