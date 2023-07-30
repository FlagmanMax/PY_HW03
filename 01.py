# List creation
list_1 = list()
list_2 = list((3.14, True, "Hello"))
list_3 = []
list_4 = [3.14, True, "Hello"]

#
# list_4.append(list_4)

#sort

my_list = [4,8,2,9,1,7,2]
sort_list = sorted(my_list)
print(my_list, sort_list, sep = '\n')

rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep = '\n')

my_list.sort()

matrix = [[1,2,3],[4,5,6],[7,8,9]]

name = 'Alex'
age = 12
text = 'Меняч зовут $s и мне %d лет'%(name, age)