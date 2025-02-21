f=open('input.txt')
l=f.readlines()
n=0
for i in l:
    for o in range(5, 0, -1):
        i=i.replace(o*'?!?!?', '1')
        i=i.replace(o*'!?!?!', '1')
        i=i.replace(o*'!?!', '1') # !?!!?! !?!
        i=i.replace(o*'?!?', '1') #?!??!? ?!?
        i=i.replace(o*'?!', '1') #?!?! ?! 
        i=i.replace(o*'!?', '1') #!?!? !?
        
    for o in range(5, 0, -1):
        i=i.replace(o*'!', '1')
        i=i.replace(o*'.', '1')
        i=i.replace(o*'?', '1')
        i=i.replace(o*'!?!', '1')
        i=i.replace(o*'?!', '1')
        i=i.replace(o*'!?', '1')
    n+=str(i).count('1')
    
print(n)
f.close()