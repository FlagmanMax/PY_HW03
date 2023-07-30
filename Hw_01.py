# Hw_01
#  Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

list_input = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5]
print(f"Input: {list_input}")

list_output = []
for i in range(len(list_input)):
    if list_input[i] not in list_output:
        if list_input.count(list_input[i]) == 2:
            list_output.append(list_input[i])
print(f"Output: {list_output}")



