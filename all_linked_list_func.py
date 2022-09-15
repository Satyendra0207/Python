
    #Class for creating node 
class Node:
        def __init__(self, data):
            self.data = data
            self.ref = None
        
    #Class for creating linked list 
class LinkedList:
        def __init__(self):
            self.head = None
        
        def print_LL(self):
            if self.head is None:
                print("Linked List is empty")
            else:
                n = self.head
                print('\n ELEMENT IN THE LLINKED LIST ARE ----\n')
                while n is not None:
                    print(n.data)
                    n = n.ref
                
        #Function to add element at begining            
        def addbegin(self, data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        
    #Function to add element at given position
        def addposition(self, newElement, position):     
            new_node = Node(newElement) 
            if(position < 1):
                print("\nposition should be >= 1.")
            elif (position == 1):
                 new_node.ref = self.head
                 self.head = new_node
            else:    
                temp = self.head
                for i in range(1, position-1):
                    if(temp != None):
                        temp = temp.ref       
                if(temp != None):
                    new_node.ref = temp.ref
                    temp.ref = new_node  
                else:
                    print("\nThe previous node is null.")
                
    #Function to add element at END  
        def addend(self,data):
            new_node=Node(data)
            val=self.head
            if self.head is None:
                self.head=new_node
                return
            else:
                while val.ref is not None:
                    val=val.ref
                val.ref = new_node
                
    # Function to search or replace element             
        def search(self,element):
            ch=False
            i=0
            if self.head is None:
                print('list is empty')
            else:
                temp=self.head
                while temp is not None:
                    i=i+1
                    if int(temp.data) == element:
                        print(f'\n ELEMENT FOUND AT LOCATION {i} IN THE LIST')
                        cho=input('\n Want to REPLACE ELEMENT Y/N - ')
                        if cho=='y'or cho=='Y':
                            val=int(input('\n ENTER THE NEW ELEMENT TO REPLACE = '))
                            temp.data=val
                            ch=True
                            break
                        else:
                            break

                    else :
                        temp=temp.ref
                        continue
            if ch==False:
                print(f'ELEMENT {element} is not in the list')
            return
                
    #Function to delete node 
        def delnode(self,remove):
            if self.head is None:
                print('\n list is empty')
            else:
                temp = self.head
                while temp is not None:
                    if (temp.data)==remove:
                        print('\n Element found in the list and will be deleted ')
                    prev=temp  
                    temp = temp.ref
                    if temp==None:
                        return
                    prev.ref=temp.ref
                    temp=None
                    ''' if temp is None:
                            prev.ref=None
                            break
                        else:
                            temp.ref=temp.ref.ref
                            break
                    temp = temp.ref'''
            return
                              
                        
    # Function to return to main menu
def back():
        ch=input('\n WANT TO RETURN TO THE MAIN MENU Y/N - ')
        if ch=='Y'or ch=='y':
                return(True)
        else:
                return(False)
            
    # MAIN PROGRAM

link1 = LinkedList()
b=True  
print('\n FIRST ENTER SOME VALUES TO START')
n= int(input('\n NO OF ELEMENTS YOU WANT TO ADD INITIALLY - '))
for i in range (n):
        link1.addend(input('\n ENTER VALUE ='))  
link1.print_LL()        
while b==True:
        print('\n \t \t ------ Welcome to Linked list ------- \t \t \n')
        print ('''\n 1.ADD ELEMENT AT BEGINING  
        \n 2.ELEMENT AT END
        \n 3.ELEMENT AT GIVEN POSITION
        \n 4.SEARCH OF ELEMENT  
        \n 5.REPLACE ELEMENT
        \n 6.DELETE ELEMENT
        \n 7.EXIT''')
        print('\nENTER YOUR CHOICE -')
        ch=int(input())
        if ch==1:
            print('\n ELEMENT AT BEGINING ')
            n= int(input('\n ENTER NO  OF ELEMENT YOU HAVE '))
            for i in range (n):
                link1.addbegin(input('\n ENTER VALUE = ')) 
            link1.print_LL()
            re=back()
            if re==True:
                continue
            else:
                break
        
        elif ch==2:
            print('\n ELEMENT AT THE END')
            n= int(input('\n ENTER NO OF ELEMENT YOU HAVE- '))
            for i in range (n):
                link1.addend(input('\n ENTER VALUE =')) 
            link1.print_LL()
            re=back()
            if re==True:
                continue
            else:
                break

        
        elif ch==3:
            print('\n --ELEMENT AT THE GIVEN POSITION --')
            n= int(input('\n ENTER ELEMENT TO ADD = '))
            m= int(input('\n ENTER POSTION AT WHICH YOU WANT TO ADD = '))
            link1.addposition(n,m) 
            link1.print_LL()
            re=back()
            if re==True:
                continue
            else:
                break

        
        elif ch==4 or ch==5 :
            print('\n SEARCH OF ELEMENT / REPLACE --')
            n = int(input('\n ENTER ELEMENT = '))
            link1.search(n) 
            link1.print_LL()
            re=back()
            if re==True:
                continue
            else:
                break

        elif ch==6:
            remove=int(input('\n Enter element to delete- '))
            link1.delnode(remove)
            link1.print_LL()
            re=back()
            if re==True:
                continue
            else:
                break

            
        elif ch==7:
            print('\n CHOOSE FOR EXIT  ')
            link1.print_LL()
            break
        
        else:
            print('\n WRONG OPTION ')
            re=back()
            if re==True:
                continue
            else:
                break
print('\n OUT FROM THE MAIN PROGRAM')
     #END OF PROGRAM