
"""
Coded by: Leyon Anderson
3/31/2026
COP3410 Assignment #5

Stacks
1.  Take the stack_ADT file and use the ArrayStack implementation and modify
    it so that the stack has a limited capacity. The maximum capacity is set to maxlen
    elements, where maxlen is a parameter to the constructor.
    Pre-allocate a list with length equal to the stack’s maximum capacity.
    If push is called when the stack is at full capacity, throw a Full exception.

2.  In the same Python file, write a recursive method for removing all the elements
    from the stack.
    Test both features using a driver function to ensure that they work properly.
    
Queues
3.  What values are returned during the following sequence of queue operations, if
    executed on an initially empty queue? enqueue(5), enqueue(3), dequeue(),
    dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(), enqueue(4),
    enqueue(2), enqueue(8), dequeue(), dequeue(), enqueue(9), enqueue(1),
    dequeue(), dequeue(). Use the Queue.py file to show the queue contents after
    every operation.
    
4.  Suppose an initially empty queue Q has executed a total of 32 enqueue operations,
    10 first operations, and 15 dequeue operations, 5 of which raised Empty errors
    that were caught and ignored. What is the current size of Q? Add your answer to
    the end of the python file.
"""

