# -- coding: utf-8 --


# 1 задание
def print_squares(n):
    i = 1
    while i**2 <= n:
        print(i**2)
        i += 1
        
        
n = int(input("Введите число n: "))
print_squares(n)



# 2 задание
def smallest_divisor(n):
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return divisor

n = int(input("Введите число n: "))
result = smallest_divisor(n)
print(result)



# 3 задание
def find_power_of_two(n):
    power = 0
    while 2 ** power <= n:
        power += 1
    power -= 1
    result = 2 ** power
    return power, result


n = int(input("Введите число n: "))
power, result = find_power_of_two(n)
print("Показатель степени:", power)
print("Сама степень:", result)



# 4 задание
def find_running_day(x, y):
    distance = x
    day = 1
    while distance < y:
        distance += distance * 0.1
        day += 1
    return day


x = int(input("Введите число x: "))
y = int(input("Введите число y: "))
running_day = find_running_day(x, y)
print(running_day)


# 5 задание
def count_sequence():
    count = 0
    while True:
        num = int(input())
        if num == 0:
            break
        count += 1
    return count

sequence_count = count_sequence()
print(sequence_count)


# 6 задание
count = 0
previous_element = None


while True:
    num = int(input("Введите натуральное число (или 0 для завершения): "))
    if num == 0:
        break
    if previous_element is not None and num > previous_element:
        count += 1
    previous_element = num


print("Количество элементов, больших предыдущего элемента:", count)



# 7 задание
max_equal_count = 0
current_equal_count = 1
previous_number = None

while True:
    num = int(input("Введите натуральное число (или 0 для завершения): "))
    if num == 0:
        break
    if num == previous_number:
        current_equal_count += 1
    else:
        if current_equal_count > max_equal_count:
            max_equal_count = current_equal_count
        current_equal_count = 1
    previous_number = num


if current_equal_count > max_equal_count:
    max_equal_count = current_equal_count

print("Наибольшее число подряд идущих элементов, равных друг другу:", max_equal_count)











