def print_user_info(name, surname, birth_year, city, email, phone):
    print(f"Имя: {name}, Фамилия: {surname}, Год рождения:"
          f" {birth_year}, Город: {city}, Email: {email}, Телефон: {phone}")

print_user_info(name="Иван", surname="Иванов", birth_year=1990,
                city="Москва", email="ivanov@mail.ru", phone="8-999-123-45-67")