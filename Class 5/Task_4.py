# Открываем файл на чтение и создаем файл для записи
with open('content.txt', 'r', ) as f_in, open('rus_content.txt', 'w') as f_out:
    # Словарь для замены английских числительных на русские
    num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}

    # Читаем файл построчно
    for line in f_in:
        # Разбиваем строку на слова
        words = line.split()

        # Заменяем английские числительные на русские в каждом слове
        for i in range(len(words)):
            if words[i] in num_dict:
                words[i] = num_dict[words[i]]

        # Создаем новую строку с измененными словами
        new_line = ' '.join(words) + '\n'

        # Записываем новую строку в файл
        f_out.write(new_line)