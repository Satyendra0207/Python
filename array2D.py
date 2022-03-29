from array import*
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
'''[11,12,5,2] refered as -0 and other array likewise '''
m=[] #another array 
print('enter value =')
c=int(input())
for j in range(4):#(just 4X4 ) 
    m.append(c)#new array store value 
T.insert(2,m) #insert new array m at 2 postion
T.append(m)#append new array m at last or end postion
T[4].insert(1,c)#element added at given index no 
T[2].insert(3,c)
T[0].append(c) #element added at last position of 
for x in T:
    print(x)
