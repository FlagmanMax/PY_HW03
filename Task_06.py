# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки


input_string = input('Введите строку: ')
input_list = sorted(input_string.split())

max_length = len(max(input_list, key=len))

# max_length = 0
# for i in input_list:
#     if len(i) > max_length:
#         max_length = len(i)
# max_length += 1
# max_length = str(max_length)

for i in range(len(input_list)):
    print(f"{i+1}.{input_list[i]: >{max_length+1}}")
    # print(f"{i + 1}.{input_list[i].rjust(max_length+1)}")
