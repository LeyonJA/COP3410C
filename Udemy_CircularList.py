'''
Taken from the Udemy course: Python for Data Structures, Algorithms and Interviews
Problem: Given a singly linked list, write a function that takes a node for the linked list and determines if the linked list is cyclic
The fucntion returns a boolean value

'''


class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


def cycle_check(node):

    # Begin both markers at the first node
    marker1 = node
    marker2 = node

    # Go until end of list
    while marker2 != None and marker2.nextnode != None:
        
        # Note
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where marker ahead reaches the end of the list
    return False


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
if __name__ == "__main__":

    # CREATE CYCLE LIST
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = a # Cycle Here!


    # CREATE NON CYCLE LIST
    x = Node(1)
    y = Node(2)
    z = Node(3)

    x.nextnode = y
    y.nextnode = z

    #RUN A CYCLE CHECK
    print(cycle_check(a))
    print(cycle_check(x))

