# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
import pprint


dict_1 = dict()
dict_1 = {'Иван':("нож", "топор", "палатка", "ложка"), \
          'Павел':("удочка", "матрац", "палатка", "ложка"), \
          'Олег':("фонарик", "ложка", "топор", "котелок", "матрац")}
print(dict_1)
list_all_things = list(dict_1.values())
list_all_names = list(dict_1.keys())

set_intersection = set(list_all_things[0])
for item in list_all_things:
    set_intersection = set_intersection.intersection(set(item))
print(f"1. Список вещей, которые взяли все: {set_intersection}")

set_unique = set(list_all_things[0])
for item in list_all_things:
    set_unique = set_unique.symmetric_difference(set(item))
print(f"2. Список уникальных вещей: {set_unique}")


# union
set_union = set(list_all_things[0])
for item in list_all_things:
    set_union = set_union.union(set(item))
print(f"3. Список всех вещей: {set_union}")

i = 0
for item1 in list_all_things:
    set_except_one = set_union.copy()
    for item2 in list_all_things:
        if item1 == item2:
            continue
        else:
            set_except_one = set_except_one.intersection(set(item2))
    set_except_one = set_except_one.difference(set_intersection)
    if len(set_except_one) > 0:
        print(f"4. {list_all_names[i]} в отличии от всех не взял {set_except_one}")
    i += 1





