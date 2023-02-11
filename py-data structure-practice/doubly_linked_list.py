class Node:
     def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class doubly_linked_list:
    def __init__(self):
        self.head = None
        
# Adding data elements
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
    
# Print the Doubly Linked list
    def listprint(self, node):
        while (node is not None):
            print(node.data)
            node = node.next
    
# Define the insert method to insert the element
    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

# Define the append method to add elements at the end
    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

# Delete the elements from the start
    def DeleteAtStart(self):
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None;
        
 # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.head.next is None:
            self.head= None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

dllist = doubly_linked_list()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.insert(dllist.head.next, 13)
dllist.listprint(dllist.head)
dllist.delete_at_end()
dllist.DeleteAtStart()
dllist.listprint(dllist.head)