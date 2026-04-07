#Doubly Linked List
#CO3410

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_after_node(self, data, prev_node):
         if prev_node is None:
             return
         new_node = Node(data)
         new_node.next = prev_node.next
         new_node.prev = prev_node
         if prev_node.next is not None:
             prev_node.next.prev = new_node
         prev_node.next = new_node

    def insert_before_node(self, data, next_node):
        if next_node is None:
            return
        new_node = Node(data)
        new_node.next = next_node
        new_node.prev = next_node.prev
        if next_node.prev is not None:
            next_node.prev.next = new_node
        else:
            self.head = new_node
        next_node.prev = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
