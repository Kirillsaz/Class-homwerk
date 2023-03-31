number = int(input("Ведите целое положительное число:"))
max_num = 0
while number != 0:
    cur_n = number % 10
    if max_num < cur_n:
        max_num = cur_n
    number = number // 10

print(f"Самая большая цифра в числе: {max_num}")
