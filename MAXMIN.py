list=[]
print('enter five values-')
for i in range(5):
    list.insert(i,int((input())))
print(list)
max= min=list[0]
for i in range(5):
    if max<list[i]:
        max=list[i]
    elif min>list[i]:
        min=list[i]
print('max =',max)
print('min =',min)
       


   

