
stack1=list()
#function to check stack for empty
def Isempty(stack5):
    if len(stack5)==0:
        print('\n Stack is empty')
        print('\n Enter element first ')
        return(0)
        
    #function to print stack
def printstack(stack2):
        x=len(stack2)
        print('\n Element in the stack:(last to first)\n')
        for i in range(x-1,-1,-1):
            print(stack2[i])
            print()
        print('\n Elements in stack first to Last -\n',stack2)
    
    #function to delete element
def oppop(stack4):
        stack4.pop()
        return(stack4)

    #function to search elemrnt
def Search(stack3,r):
        check=False
        x=len(stack3)  
        for i in range(x-1,-1,-1):
                if r==stack3[i]:
                    print(f"\n Entered element {r} found at {i} location in the stack")
                    print('''\n Enter \n 1-Replace \n 2-Delete \n 3-NONE \n ''')
                    cho=int(input())
                    check=True
                    if cho==1:
                        print('\n Enter new element to replace old one- ')
                        value=int(input())
                        stack3[i]=value   
                    elif cho==2:
                        print("\n Want to delete element Y/N")
                        b=input()
                        if b=='Y'or b=='y':
                            for j in range(i,x-1,1):
                                stack3[j+1],stack3[j]= stack3[j],stack3[j+1]
                            stack3=oppop(stack3)
                    else:
                        break
        if check==True:
            printstack(stack3)
        else:
            print('\n Entered element {r} not found in the stack ')
        return(stack3)
        
    #main program

choice='Y' 
while choice=='Y' or choice=='y':
        print('\n \t STACK OPERATIONS \t \n ')
        print(''' 1- CHECK FOR UNDERFLOW \n 2- INSERT ELEMENT \n 3- DELETE ELEMENT \n 4- SEARCH ELEMENT \n 5- COUNT ELEMENT 
        \n Enter your choice - ''')
        ch=int(input())
        if ch==1:
            s=Isempty(stack1)
        
        elif ch==2:
            print('\n Enter no of element you want to enter - ')
            no=int(input())
            print('\n Enter elements -\n')
            for i in range(no):
                m=int(input())
                stack1.append(m)
            printstack(stack1)
            choice=input('\n Want to perform more operations-Y/N = ')
            if choice=='Y' or choice=='y':
                continue
            else:
                break

        elif ch==3:
            print('\n\t DELETE MENU \t\n')
            u=Isempty(stack1)
            if u==0:
                continue
            else:
                s=int(input('enter element want to Delete in stack = '))
                stack1=Search(stack1,s)
                choice=input('\n Want to perform more operations-Y/N = ')
                if choice=='Y' or choice=='y':
                    continue
                else:
                    break

        elif ch==4:
            print('\n\t SEARCHING MENU \t\n')
            u=Isempty(stack1)
            if u==0:
                continue
            else:
                s=int(input('enter element want to search in stack = '))
                stack1=Search(stack1,s)
                choice=input('\n Want to perform more operations-Y/N = ')
                if choice=='Y' or choice=='y':
                    continue
                else:
                    break
        elif ch==5:
            u=Isempty(stack1)
            if u==0:
                continue
            else:
                print('\n No of element present in stack-',len(stack1))
                printstack(stack1)
                choice=input('\n Want to perform more operations-Y/N = ')
                if choice=='Y' or choice=='y':
                    continue
                else:
                        break
        else:
            print('\n Not valid selection')
            choice=input('\n Want to go to main menu -Y/N = ')
            if choice=='Y' or choice=='y':
                continue
            else:
                break
printstack(stack1)
print('\n OUT from Stack operations ')
