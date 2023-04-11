def calculate_salary(hours, rate, bonus):
    salary = (hours * rate) + bonus
    return salary

hours = float(input("Введите выработку в часах: "))
rate = float(input("Введите ставку в час: "))
bonus = float(input("Введите премию: "))

total_salary = calculate_salary(hours, rate, bonus)

print("Заработная плата сотрудника составляет:", total_salary)
