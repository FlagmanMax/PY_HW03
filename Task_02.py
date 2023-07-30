# Задание №2
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

input_string = ''
while not input_string:
    input_string = input('Введите строку:')
    if input_string.isdigit():
        print('Целое положительное', int(input_string))
    else:
        try:
            print('Вещественное: ', float(input_string))
        except:
            if any(i.isupper() for i in input_string):
                print('В строке есть заглавные: ',input_string.upper())
            else:
                print('В строке нет заглавных: ', input_string.lower())
