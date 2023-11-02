# -- coding: utf-8 --


# 10 вариант 
# 1 задание
def check_duplicates(lst):
    unique_elements = set(lst)
    if len(unique_elements) < len(lst):
        duplicates = [x for x in unique_elements if lst.count(x) > 1]
        return duplicates
    else:
        return None

user_input = input("Введите элементы списка через пробел: ")
user_list = user_input.split()

result = check_duplicates(user_list)

if result:
    print("Повторяющиеся элементы:", result)
else:
    print("Повторяющихся элементов нет.")



# 2 задание

my_array = []


for _ in range(15):
    element = int(input("Введите элемент массива: "))
    my_array.append(element)


for i in range(len(my_array)):
    if my_array[i] < 10:
        my_array[i] = 0
    elif my_array[i] > 20:
        my_array[i] = 1
