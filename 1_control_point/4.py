# -- coding: utf-8 --

#1 задание 
a = int(input("Введите 1 число "))
b = int(input("Введите 2 число "))
for i in range(a, b + 1):
    print(i)




#2 задание 
a = int(input("Введите 1 число "))
b = int(input("Введите 2 число "))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)



#3 задание 
a = int(input("Введите 1 число "))
b = int(input("Введите 2 число "))
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')




#4 задание 
a = int(input("Введите 1 число "))
b = int(input("Введите 2 число "))
for i in range(a|1, b+1, 2): 
    print(i, end=' ')



#5 задание 
a = int(input("Введите число "))
sum = 0
for i in range(1, a + 1):
    sum += i ** 3
    print(sum)



#6 задание 
a = int(input("Введите число "))
res = 1
for i in range(1, a + 1):
    res *= i
print(res)




#7 задание 
def factorial_sum(a):
    sum = 0
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
        sum += factorial
    return sum

a = int(input("Введите число  "))
result = factorial_sum(a)
print("Сумма факториалов = ", result)



#8 задание 
a = int(input("Введите число  "))
for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()



#9 задание 
n = int(input("Введите количество чисел из ряда Фибоначчи: "))
fibonacci_sum = 0
a, b = 0, 1
count = 0

while count < n:
    fibonacci_sum += a
    a, b = b, a + b
    count += 1

print("Сумма чисел из ряда Фибоначчи:", fibonacci_sum)




#10 задание 
n = int(input("Введите количество чисел из ряда Фибоначчи: "))
k = int(input("Введите порядковый номер числа, с которого нужно начать: "))

sum = 0
count = 0

fib1 = 0
fib2 = 1

for i in range(1, n+1):
    current_num = fib1 + fib2
    sum += current_num
    
    if i >= k:
        count += 1

    if count == n:
        break
        
    fib1 = fib2
    fib2 = current_num

print("Сумма чисел ряда Фибоначчи, начиная с порядкового номера", k, ":", sum)














