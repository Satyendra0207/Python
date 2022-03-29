import numpy as np
m= np.array([['satyendra singh',21,45,46,47],['Aneesh',22,46,48,47 ],['Aditya soni',21,48,48,49]])
a=len(m)
sum=0
w=0
print('\n for age comparison press-1 and \n for sum of marks press 2')
z=input()
if z=='1':
    print('enter age you want to check-')
    age=int(input())
    print(f'details of student whoose age is {age}-\n')
    for i in range (a):
            b=int(m[i][1])
            if age==(b):
              print(m[i])        
else:
    print('\n enter student name whoose marks you want to calculate-')
    d=str(input())
    for i in range(a):
        x=str(m[i][0])
        if d==x:
            w=3 
            for t in range(2,5):
                x=str(m[i][t])
                sum+=int(x)
    if w==3:           
        avg=sum/3      
        print(f'\n sum of the marks entered student {d} are =\n',sum)
        print('Average of marks=',avg)
    else:
        print('\n name not found in the list ')
print('\n Given values \n',m)
