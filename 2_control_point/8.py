# -- coding: utf-8 --


# 10 вариант 
# 1 задание
a = int(input("Введите цифру a: "))
b = int(input("Введите цифру b: "))
c = int(input("Введите цифру c: "))

count = 0

N = int(input("Введите число N (210 < N < 231): "))

for num in range(100, N+1):
    digits = set(str(num))
    if str(a) in digits and str(b) in digits and str(c) in digits:
        count += 1

print("Количество чисел, составленных из цифр", a, b, c, "в диапазоне [100, N]:", count)



# 2 задание
sentence = input("Введите строку слов: ")
words = sentence.split() 
reversed_words = list(reversed(words)) 
reversed_sentence = " ".join(reversed_words)  
print(reversed_sentence)  
