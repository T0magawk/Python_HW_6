# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def find_indexes_in_range(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes

# Вводим элементы массива 
n = int(input("Введите количество элементов : "))
lst = []
for i in range(n):
    element = int(input("Введите элемент {}: ".format(i+1)))
    lst.append(element)

min_val = int(input("Минимум : "))
max_val = int(input("Максимум : "))

# Поиск нужных элементов
indexes_in_range = find_indexes_in_range(lst, min_val, max_val)

# Выводим список получившихся элементов
print("Элементы списка, удовлетворяющие поиску:", indexes_in_range)
