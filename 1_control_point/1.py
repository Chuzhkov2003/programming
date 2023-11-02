# -- coding: utf-8 --

# 1 задание
print ("Курс Основы программирования начался")


# 2 задание
print("Остаток от деления 16823 * 12302 / 3092 = ", 16823 * 12302 % 3092 )


# 3 задание
age = int(input("Введите ваш возраст : "))

if (74>age>0):
    print("Вы не слишком стар или молод")
else :
    print("Вы слишком стар или молод")
    exit ()

if (age>=16):
    print("Поздравляем вы поступили в ВГУИТ")

    name = input("Введите имя абитуриента: ")
    if name != "Иван":
        print("Вы не Иван!")
    else:
        print("Вы Иван!!!")
        exit()

else:
    print("Сначала нужно окончить школу!")
    print("Вам осталось учиться ", 16 - age, "лет")
    exit()


# 4 задание
    seconde = int(input("Введите число n: "))

minute = seconde/60
hour = minute/60
days = hour/24

print ("Это", days,":",hour,":", minute,":",seconde)



# 5 задание
n = int(input("Введите число n: "))

result = n + n**2 + n**3 + n**4 + n**5
print(result)


# 6 задание
x = input("Введите значение x : ")
y = input("Введите значение y : ")
z=x
x=y
y=z
print("Значение x = ", x)
print("значение y =  ", z)


# 7 задание
number = int(input("Введите number: "))
if number % 2 == 0:
    print('number четное число')
else:
    print('number нечентное число')






