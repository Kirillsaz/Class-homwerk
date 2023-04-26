with open('content.txt', 'r', encoding='utf-8') as f:
    sum = 0
    for line in f:
        for num in line.split():
            if num == '1' or num == '2':
                sum += int(num)
    print('Сумма чисел: ', sum)
    