
f = open('inputt.txt', 'r', encoding='utf-8')
s = list(f.read())
glas = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ъ']
for i in range(len(s)):
    if (i != 0):
        if (s[i] in glas) and (s[i - 1] in sogl):
            s[i] = str(s[i] + "с" + s[i])
print(''.join(str(x) for x in s))
f.close()