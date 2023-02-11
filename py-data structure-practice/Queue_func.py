
myqueue=list()
    #function to check underflow
def Isempty(queue4):
        if len(queue4)==0:
            print('\n UNDERFLOW CONDITION / QUEUE IS EMPTY')
            print('\n Enter element first ')
            return(0)
        
     #Function to Delete element from Queue
def Dequeue(queue2,j):
        #t=j
        queue2.pop(j)
        return(queue2)

    #function to search element
def Search(queue1,r): 
        d=len(queue1)
        check=False
        for i in range(d):
            if queue1[i]==r:
                print(f"\n Entered element {r} found at {i+1} location in the QUEUE")
                print('''\n Enter \n 1-Replace \n 2-Delete \n 3-NONE \n ''')
                cho=int(input())
                check=True
                if cho==1:
                    print('\n Enter new element to replace old one- ')
                    value=int(input())
                    queue1[i]=value   
                elif cho==2:
                    print("\n Want to delete element Y/N")
                    b=input()
                    f=i
                    if b=='Y'or b=='y':
                        print(i)
                        queue1=Dequeue(queue1,f)
                else:
                    break           
        if check==True:
            return(queue1)
        else:
            print(f'\n Entered Element {r} Not found in the QUEUE')
            return(queue1)

    #function to enter value in queue
def enqueue(queue3,n):
        for i in range(n):
            m=int(input())
            queue3.append(m)
        return(queue3)
        
    #main program

choice='Y' 
while choice=='Y' or choice=='y':
        print('\n \t QUEUE OPERATIONS \t \n ')
        print(''' 1- CHECK FOR UNDERLFLOW \n 2- INSERT ELEMENT
 3- DELETE ELEMENT \n 4- SEARCH ELEMENT \n 5- COUNT ELEMENT \n 6- Empty QUEUE
        \n Enter your choice - ''')
        ch=int(input())
        if ch==1:
            Isempty(myqueue)
        elif ch==2:
            print('\n Enter no of element you want to enter - ')
            no=int(input())
            print('\n Enter elements -\n')
            myqueue=enqueue(myqueue,no)
            print('\n QUEUE= ',myqueue)
            choice=input('\n Want to perform more operations-Y/N = ')
            if choice=='Y' or choice=='y':
                continue
            else:
                break

        elif ch==3 or ch==4:
            print('\n\t MENU FOR SEARCH AND DELETE \t\n')
            x=Isempty(myqueue)  
            if x==0:
                continue
            else:
                s=int(input('Enter element want to Search or Delete in QUEUE = '))
                myqueue=Search(myqueue,s)
                print('\n QUEUE= ',myqueue)
                choice=input('\n Want to perform more operations-Y/N = ')
                if choice=='Y' or choice=='y':
                    continue
                else:
                    break
    
        elif ch==5:
            u=Isempty(myqueue)
            if u==0:
                continue
            else:
                print('\n No of element present in stack-',len(myqueue))
                print('\n QUEUE= ',myqueue)
                choice=input('\n Want to perform more operations-Y/N = ')
                if choice=='Y' or choice=='y':
                    continue
                else:
                    break
        elif ch==6:
            print('\n All element of Queue will be removed')
            print('\n QUEUE= ',myqueue)
            s=len(myqueue)
            k=0
            while k<s:
                myqueue.pop()
                k=k+1
                continue
                print('\n Queue is Emptied')
                print(myqueue)
                u=Isempty(myqueue)

        else:
            print('\n Not valid selection')
            choice=input('\n Want to go to main menu -Y/N = ')
            if choice=='Y' or choice=='y':
                continue
            else:
                break
print('\n QUEUE= ',myqueue)
print('\n OUT from QUEUE operations ')

    
