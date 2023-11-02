# -- coding: utf-8 --

#1 задание 

num1 = int(input("Введите 1 число "))
num2 = int(input("Введите 2 число "))
num3 = int(input("Введите 3 число "))
print("Сумма = ", num1 + num2 + num3)


#2 задание 
a = int(input("Введите 1 катет "))
b = int(input("Введите 2 катет "))
print("Площадь прямоугльного  треугольника =  ", 0.5*a*b)


#3 задание
n = int(input("Введите количество минут: "))  
if n>86400:
    print("Слишком много минут!!!")
    exit()

hours = n // 60  
minutes = n % 60  

print("На электронных часах будет показываться:", hours, "часа", minutes, "минуты")



#4 задание
def length(a, b, a2, b2):
    
    print("Длинна шнурка равна ", 2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)
    

a = int(input("Расстояние между рядами равно  "))
b = int(input("Расстояние между дырочками в ряду равно "))
N = int(input("Количество дырочек в каждом ряду равно "))
l = int(input("длина свободного конца шнурка равна "))

length(a, b, l, N)




#5 задание
def find_minimum(a, b, c):
    minimum = a
    
    if b < minimum:
        minimum = b
    
    if c < minimum:
        minimum = c
    
    print("Наименьшее число:", minimum)

a = int(input("Введите 1 число "))
b = int(input("Введите 2 число "))
c = int(input("Введите 3 число "))

find_minimum(a, b, c)  




#6 задание
def check(a, b, a2, b2):
    
    if (a+b+a2+b2) % 2 == 0:
        print('Да')
    else:
        print('Нет')

a = int(input("Введите номер столбца для 1 клетки "))
b = int(input("Введите номер строки для 1 клетки "))
a2 = int(input("Введите номер столбца для 2 клетки "))
b2 = int(input("Введите номер строки для 2 клетки "))

check(a, b, a2, b2)




#7 задание
def year(a):
    
    if a % 400 == 0:
        print("Год высокосный")
    elif a % 4 == 0 and a % 100 != 0:
        print("Год высокосный")
    else:
        print("Год не высокосный")
   

a = int(input("Введите год "))
year(a)   




#8 задание
def find_numbers(a, b, c):
    if a == b and b == c: 
        print("3")
    elif a == b or b == c or a == c:  
        print("2")
    else:  
        print("0")
        
    
a = int(input("Введите 1 число "))
b = int(input("Введите 2 число "))
c = int(input("Введите 3 число "))
find_numbers(a, b, c)




#9 задание
def check(n, m, k):
    
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print('Да')
    else:
        print('Нет')

n = int(input("Введите 1 число "))
m = int(input("Введите 2 число "))
k = int(input("Введите 3 число "))     

check(n, m, k)





