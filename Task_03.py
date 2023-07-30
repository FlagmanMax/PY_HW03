# Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа
from pprint import pprint

tuple_1 = (1, 'one', 3.14, True, [1, 2, 3], 4-3j,False)
print(*tuple_1)

dict_1 = {}
for i in tuple_1:
    if type(i).__name__ not in dict_1:
        dict_1[type(i).__name__] = []
    dict_1[type(i).__name__].append(i)

pprint(dict_1)