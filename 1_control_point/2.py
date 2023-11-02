# -- coding: utf-8 --
#4 задание

import math

x = float(input('Введите число x:'))
y = float(input('Введите число y:'))
z = float(input('Введите число z:'))

s = (abs(math.cos(x)-math.cos(y))**(1+2*math.sin(y)**2))*(1+z+math.pow(z,2)/2+math.pow(z,3)/3+math.pow(z,4)/4)

print (s)




#5 задание
import math

x = float(input('Введите число x:'))
y = float(input('Введите число y:'))
z = float(input('Введите число z:'))

s = math.log1p(pow(y,-math.sqrt(abs(x))))*(x-y/2)+math.sin(math.atan(z))**2

print (s)




#5 задание

import math

x = float(input('Введите число x:'))
y = float(input('Введите число y:'))
z = float(input('Введите число z:'))

s = 5*math.atan(x)-1/4*math.acos(x)*(x+3*abs(x-y)+x**2)/(abs(x-y)*z+x**2)

print (s)


