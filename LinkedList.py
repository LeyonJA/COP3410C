''''
Single Linked List Implementation
COP3410
Sareh Taebi
'''
class Node:
    '''Lightweight class for storing a singly linked node.'''

    def __init__(self, element):    # initialize node’s field
       self.element = element                   # reference to user’s element
       self.next = None                   # reference to next node 

   
class LinkedList:
    def __init__(self):
        self.head = None
        self.size  = 0

    def traverse(self):
        current = self.head
        while current:
            print(current.element)
            current = current.next    #traversal


    def add_first(self,e):
        newest = Node(e)        #create new node instance storing reference to element e
        newest.next = self.head    #set new node’s next to reference the old head node
        self.head = newest         #set variable head to reference the new node
        self.size = self.size+1       #increment the node count

    def add_last(self,e):
        newest = Node(e)        #create new node instance storing reference to element e
        newest.next = None      #set new node’s next to reference the None object

        if self.head is None:
            self.head = newest

        current = self.head
        while current.next:
            current = current.next
        current.next = newest
        
        self.size = self.size+1       #increment the node count


    def remove_first(self):
        if self.head is None:
            raise Exception ("The list is empty")
        self.head.element = None    #Garbage Collection
        self.head = self.head.next    #make head point to next node (or None)
        self.size = self.size - 1     #decrement the node count


    def remove_last(self):
        if self.head is None:
            raise Exception ("The list is empty")

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None
        self.size = self.size - 1     #decrement the node count
            

    def __str__(self):
        temp = self.head
        node_content = []
        while temp:
            node_content.append(temp.element)
            temp = temp.next
                
        return(str(node_content)[1:-1])
        
if __name__ == "__main__":

    LL = LinkedList()  #empty 
    LL.head = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    
    LL.head.next= Node2
    Node2.next = Node3
    Node3.next = Node4
    
    LL.traverse()   #pay attention to the cost of this function
    LL.add_first("Head")
    LL.add_last("Tail") #pay attention to the cost of this function
    print(LL)
    LL.remove_first()
    print(LL)
    LL.remove_last() #pay attention to the cost of this function
    print(LL)


    
    
