'''
COP3410 - FAU
Doubly Linked List Base and Deque Implementation
Date: 11/23/2022
'''

class DoublyLinkedBase:
    '''A base class providing a doubly linked list representation. This class should not be used publicly'''

    class Node:
        '''Lightweight, nonpublic class for storing a doubly linked node.'''

        def __init__(self, element, prev, next): # initialize node’s field

            self.element = element   # user’s element
            self.prev = prev         # previous node reference
            self.next = next         # next node reference

    def __init__ (self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer # trailer is after header
        self.trailer.prev = self.header # header is before trailer
        self.size = 0 # number of elements

    def __len__ (self):
        '''Return the number of elements in the list.'''
        return self.size

    def is_empty():
        return self.size == 0

    def insert_between(self, e, predecessor, successor):
        '''Add element e between two existing nodes and return new node.'''
        newest = self.Node(e, predecessor, successor) # linked to neighbors
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest    #just because we like to 

    def delete_node(self, node):
        '''Delete nonsentinel node from the list and return its element.'''
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element      # record deleted element
        node.prev = node.next = node.element = None   # deprecate node
        return element


# USING THE DOUBLY LINK BASE CLASS FOR IMPLEMENTAION OF DEQUES

class LinkedDeque( DoublyLinkedBase): # note the use of inheritance
    '''Double-ended queue implementation based on a doubly linked list.'''
    
    class Empty(Exception):
        '''Error attempting to access an element from an empty container.'''
        pass
    
    def first(self):
        '''Return (but do not remove) the element at the front of the deque.'''
        if self.is_empty( ):
           raise Empty("Deque is empty")
        return self.header.next.element # real item just after header
    
    def last(self):
        '''Return (but do not remove) the element at the back of the deque.'''
        if self.is_empty( ):
          raise Empty("Deque is empty")
        return self.trailer.prev.element # real item just before trailer
   
    def insert_first(self, e):
        '''Add an element to the front of the deque.'''
        self.insert_between(e, self.header, self.header.next) # after header
        
    def insert_last(self, e):
        '''Add an element to the back of the deque.'''
        self.insert_between(e, self.trailer.prev, self.trailer) # before trailer

    def delete_first(self):
        '''Remove and return the element from the front of the deque.
    
        Raise Empty exception if the deque is empty.
        '''
        if self.is_empty(self):
            raise Empty("Deque is empty")
        return self.delete_node(self.header.next) # use inherited method
 
    def delete_last(self):
            '''Remove and return the element from the back of the deque.
            Raise Empty exception if the deque is empty.
            '''
            if self.is_empty( ):
                raise Empty("Deque is empty")
            return self.delete_node(self.trailer.prev) # use inherited method

if __name__ == "__main__":
    LD = LinkedDeque();
    LD.insert_first("End ");
    LD.insert_last("Of ");
    LD.insert_last("Semester ");
    LD.insert_last("Approaching");
    LD.insert_first("Soon enough ");
    LD.insert_last("!");

    
