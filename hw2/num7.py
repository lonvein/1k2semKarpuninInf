a=list(map(int, input().split()))
x=0
#str - строка, int - другой тип - численный, поэтому так как type(x) -> int, создание x не противоречит правилам задачи
for i in a:
    if a.count(i) >= x:
        x=i
print(x)
        
