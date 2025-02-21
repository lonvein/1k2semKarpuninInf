'''3. В этой задаче вам даётся три списка студентов:
- владеющих французским языком
- умеющих плавать
- владеющих игрой на фортепиано
Вам необходимо определить список пловцов-пианистов, не владеющих французским.
Формат входных данных
Три строки. В каждой через пробел записаны номера зачёток студентов. Первая строка посвящена владеющим французским, вторая пловцам и третья пианистам.

Формат выходных данных: Одна строка c номерами зачёток через пробел по возрастанию.

Примеры:

Ввод данных:

1 2 5 7 8 9

3 4 8 2 10

10 3 2 8 5

Вывод данных:

3 10
'''

fr = sorted(list(map(int, input().split()))) # no
sw = sorted(list(map(int, input().split()))) # yes
pi = sorted(list(map(int, input().split()))) # yes

swpi = []
for i in sw:
    for j in pi:
        if i == j:
            swpi.append(i)
swpi = list(set(swpi))
print(swpi)

ans = []
for i in swpi:
    if not(i in fr):
        ans.append(i)
ans = sorted(ans)
ans_s = ''
for i in ans:
    ans_s = ans_s + str(i) + ' '
print(ans_s[:-1])