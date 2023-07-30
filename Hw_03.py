# Hw_03
# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
import random

dict_staff = {"вещь_01": 10, "вещь_02": 11, "вещь_03": 12, "вещь_04": 13, "вещь_05": 14, "вещь_06": 15, "вещь_07": 16}

load_max = 50

wieght = 0

res = []
while wieght < load_max:
    key, value = random.choice(list(dict_staff.items()))
    if (key, value) in res:
        continue
    if wieght + value > load_max:
        break
    wieght += value
    res.append((key, value))

print(*res, sep='\t\t')
print(f"Общий вес = {wieght} кг")