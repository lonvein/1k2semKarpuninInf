'''5. Напишите функцию, которая принимает на вход
строку и tag для HTML и выводит строку заключённую
в нужный тег. К HTML элементам (тегам) отнесите 
следующие: a, abbr, b, body, caption, cite, code, 
div, form, h1, h2, h3, h4, h5, h6, header, i и s. 
Если в качестве тега введен отличный от вариантов
выше, то вывести "Введён неверный тег".

Пример:

Входные данные:

i

Python

Выходные данные:

<i>Python</i>'''


tags = ['a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's']
tag = str(input())
string = str(input())
if tags.count(tag) == 1:
    print(f'<{tag}>{string}</{tag}>')
else:
    print("Введён неверный тег")