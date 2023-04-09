total_sum = 0

while True:
    num_string = input("Введите числа, разделённые пробелом: ")

    if num_string == "stop" or num_string == "стоп":
        break

    try:
        nums = [int(num) for num in num_string.split()]
        sum_nums = sum(nums)
        total_sum += sum_nums
        print("Сумма введённых чисел: ", sum_nums)
        print("Общая сумма: ", total_sum)
    except ValueError:
        print("Некорректный ввод. Попробуйте ещё раз.")
