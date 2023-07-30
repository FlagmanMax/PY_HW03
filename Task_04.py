# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

list_01 = [1, 2, 2, 3, 3, 3, 4, 5, 7, 5, 1]
print(list_01)

# for i in list_01:
#     if list_01.count(i) == 2:
#         list_01.remove(i)
#         list_01.remove(i)

i = 0
while i < len(list_01):
    if list_01.count(list_01[i]) == 2:
        temp = list_01[i]
        list_01.remove(temp)
        list_01.remove(temp)
    else:
        i += 1
print(list_01)


