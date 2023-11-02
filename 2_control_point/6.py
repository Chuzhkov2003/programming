# -- coding: utf-8 --


# 10 вариант 

sentence = input("Введите строку-предложение на английском языке: ")
words = sentence.split()  
capitalized_words = [word.capitalize() for word in words]  
transformed_sentence = " ".join(capitalized_words)  
print(transformed_sentence)  