# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка

#  *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

list_1 = [1, 1, 2, 2, 3, 4]
print(*list_1)

set_1 = set(list_1)
print(*set_1)

list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(*list_2)