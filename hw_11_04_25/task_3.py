'''3. Напишите функцию, которая принимает на вход две строки и выводит одну строку, 
в которой для первых 2-х символов строк последовательность символом обратная и строки разделены символом '-'.

Пример:

Входные данные:

abc
xyzqw

Выходные данные:

bac-yxzqw'''

a = str(input())
b = str(input())
print(f'{a[0:2][::-1]}{a[2:]}-{b[0:2][::-1]}{b[2:]}')