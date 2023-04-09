def int_func(word):
    return word.capitalize()

def capitalize_string(string):
    words = string.split(" ")
    capitalized_words = [int_func(word) for word in words]
    return " ".join(capitalized_words)

input_string = input("Введите строку: ")
output_string = capitalize_string(input_string)
print(output_string)
