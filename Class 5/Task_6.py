# Открываем файл с информацией о занятиях
with open('lessons.txt', 'r') as file:
    # Создаем пустой словарь
    lesson_dict = {}
    # Читаем файл построчно
    for line in file:
        # Разбиваем строку на список по разделителю "-"
        lesson_info = line.split(" - ")
        # Извлекаем название предмета и количество занятий
        name = lesson_info[0]
        info = lesson_info[1].strip()
        # Создаем список из количества занятий по каждому типу
        info_list = [int(x.split(": ")[1]) for x in info.split(", ")]
        # Суммируем количество занятий по всем типам
        total = sum(info_list)
        # Добавляем предмет и количество занятий в словарь
        lesson_dict[name] = total

# Выводим сформированный словарь на экран
print(lesson_dict)