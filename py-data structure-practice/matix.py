import numpy as np
m=([['satyendra singh',21,45,46,47],['Aneesh',21,46,48,47 ],['Aditya soni',21,48.48,49]])
m.append(['Anmol Malviya',21,45,43,23])
m.append(['Sunidhi',21,45,46,47])
b=False
mat=[]
def printdat(s):
    for i in range(len(s)):
        print(s[i],'\n')
def adddetails(m):
        print('enter the name of student -\n')
        mat.append(input())
        print('enter the age of student -\n')
        mat.append(int(input()))
        print('enter the marks  of student in 3 subject -\n')
        for j in range(3):
            mat.append(int(input()))
        m.append(mat)
        print('Want to enter more-Y/N--')
        p=input()
        if p=='y'or p=='y':
            adddetails()
        else:
            return(p)

def search1(nam):
    b=False
    a=len(m)
    for i in range(a):
        if str(m[i][0])==str(nam):
            print(m[i][0])
            print('\n Name found at location-',i,0)
            print('\n Other details are -')
            for j in range(a):
                print(m[i][j])
            b=True
    if b==False:
        print(f'\n entered name {nam} not found in the list \n ')
    print('\n want to serch more-y/n')
    c=input()
    if c=='y'or c=='Y':
        return(True)
    else :
        return(False)
       
  
choice='y'        
printdat(m)
while choice=='y' or choice=="y":
    dict={1:"Entry",2:"Searching",3:"Sum an average",4:'Exit'}
    for i in dict:
         print(f"\n {i}-{dict[i]}\n")
   
    cho=int(input('\n Choose from these options--'))
    
    if cho==1:
        print("ENTRY OF VALUE ")
        r=adddetails(m)
        if r=='N' or r=='n':
            printdat(m)
            continue

    elif cho==2:
        print('\n Searching')
        print('Want to search name in list the - Y/N--')
        d=input()
        while d=='y'or d=="Y":
            print('\n Enter name you want to search -\n')
            t=search1(input())
            na=input()
            if t==True:
                printdat(m)
                continue 
            else:
                print('\n Out from searching')
                printdat(m)
                print('\n Want to perform more operations Y/N')
                k=input()
                if k=='y'or k=='Y':
                    continue 
                else:
                    break
    elif cho==3:
        print('\n SUM or Average')
        print('\n Enter student name whoose marks you want to calculate-')
        d=str(input())
        sum=0
        for i in range(len(m)):
            x=str(m[i][0])
            if d==x:
                w=3 
                for t in range(2,5):
                    x=int(str(m[i][t]))
                    sum=sum+x
        if w==3:           
            avg=sum/3      
            print(f'\n sum of the marks entered student {d} are =\n',sum)
            print('Average of marks=',avg)
        else:
            print('\n Name not found in the list ')
    else:
        break
print('\n You are out from here -Thank you for choosing us')
      
    
            
