from array import *
def arraycalc():
    a=array('i',[])
    b=True 
    while b==True:
        print('\n \t \t ------ Welcome to ARRAY wizard ------- \t \t \n')
        print ('''\n 1.ADD ELEMENT TO ARRAY  
        \n 2.DELETE ELEMENT 
        \n 3.REPLACE ELEMENT
        \n 4.SORTING 
        \n 5.SEARCH OF AN ELEMEMT
        \n 6.EXIT''')
        print('\nENTER YOUR CHOICE(firstly enter elements for better results) -')
        ch=int(input())
        if ch==1:
            print('\nEnter no of element you want to add in the list -')
            n=int(input())
            print('\nEnter elements one by one-')
            for i in range(n):
                x=int(input())
                a.append(x)
            print(a)  
            print('\n Now Other OPTIONS are available  ')
            continue

        elif ch==2 or ch==3 or ch==5:
            print(a)
            print('\nEnter choice \n A= For (Delete / Search) Element   \n B= For Replace Element ')
            choi=input()
            if choi=='A'or choi=='a':
                print('\nEnter element which you want to Delete or Search =')
                c=int(input())
                for i in range(len(a)-1):
                    if c==a[i]:
                        print(f'\n Entered element {c} found at location {i} in the array')
                        print('\nWant to delete the element Y/N-')
                        r=input()
                        if r=='Y' or r=='y':
                            a.remove(a[i]) 
                        b=False
                if b==True:
                    print(f'\n ELement {c} not found in array')
                print(a)
            else:
                print('\nEnter element which you WANT to REPLACE and the NEW NO to Replace =')
                c=int(input())
                d=int(input())
                for i in range(len(a)-1):
                    if c==a[i]:
                        print(f'\nElement {c} found at this location {i} will be replaced from array')
                        a[i]=d
                        print(a)
                if b==True:
                    print(f'\n ELement {c} not found in array')
            print('\nWant to perform more function on array-Y/N')
            cho=input()
            if cho=='y'or cho=='Y':
                continue
            else:
                break
            
        elif ch==4:
            print('\n \t *** Welcome to sorting wizard *** \t')
            print('\nArray Before sorting(Arranging) \n','\n',a)
            print('\nEnter choice for 1-ascending order    2- descending  order') 
            s=int(input())
            m=len(a)
            if s==1:                                    #Bubble sort 
                for j in range(m):
                    for i in range(0,m-j-1):
                        if a[i]>a[i+1]:
                            a[i],a[i+1]=a[i+1],a[i]
                print('\nArray after Sorting(arranging) in ascending order \n')
                print(a,'\n')
            else:
                for j in range(m):
                    for i in range(0,m-j-1):
                        if a[i]<a[i+1]:
                            a[i],a[i+1]=a[i+1],a[i]
                print('\nArray after Sorting(arranging) in descending order\n')
                print(a,'\n')
            print('\nWant to perform more function on array-Y/N')
            cho=input()
            if cho=='y'or cho=='Y':
                continue
            else:
                break
        
        elif ch==6:
            break
        break                

    print('''\n \t YOU ARE OUT FROM ARRAY'S MAIN WIZARD 
    \n \t THANK YOU FOR CHOOSING US ''')
arraycalc()
