from typing import List


class Btree:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    #insert
    def insertval(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left is None:
                self.left=Btree(data)
            else:
                self.left.insertval(data)
        elif data>self.data:
            if self.right is None:
                self.right=Btree(data)
            else:
                self.right.insertval(data)
        else:
            self.data= data
            
    #print 
    def printval(self):
        if self.left:
            self.left.printval()
        print(self.data)
        if self.right:
            self.right.printval()
            
    # In-Order traversal
    def In_order(self):
        # LRoR -first left 
        
        list1=[]
        if self.left:
            list1+=self.left.In_order()
            
        # root node after left side
        list1.append(self.data)
        
        #right nodes
        if self.right:
            list1+=self.right.In_order()    
        return list1     
    
    #Pre-Order traversal (RoLR)
    def pre_order(self):
        list1=[]
        list.append(self.data)
        if self.left:
            list1+=self.left.pre_order()
        if self.right:
            list1+=self.right.pre_order()
    
    #Post-Order traversal(LRRo)
    def post_order(self):
        list1=[]
        if self.left:
            list1+=self.left.post_order()
        if self.right:
            list1+=self.right.pre_order()
        list1.append(self.data)
        
    def searchval(self,val):
        if val==self.data:
            return True
        elif val<self.data:
            self.left.searchval(val)
        elif val>self.right:
            self.right.searchval(val)
        else:
            return False
        
        
            
        
root=Btree(10)
root.insertval(4)
root.insertval(1)
print(root.searchval(10))
root.printval()
        