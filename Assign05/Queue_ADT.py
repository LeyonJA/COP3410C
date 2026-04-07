"""
Coded by: Leyon Anderson
modifying the provided Queue_ADT.py script to answer the following tasks.
4/06/2026
COP3410 Assignment #5

Queues
3.  What values are returned during the following sequence of queue operations, if
    executed on an initially empty queue? enqueue(5), enqueue(3), dequeue(),
    enqueue(2), enqueue(8), dequeue(), dequeue(), enqueue(9), enqueue(1),
    dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(), enqueue(4),
    dequeue(), dequeue(). Use the Queue.py file to show the queue contents after
    every operation.

4.  Suppose an initially empty queue Q has executed a total of 32 enqueue operations,
    10 first operations, and 15 dequeue operations, 5 of which raised Empty errors
    that were caught and ignored. What is the current size of Q? Add your answer to
    the end of the python file.
"""

class ArrayQueue:
    '''FIFO queue implementation using a Python list as underlying storage.'''
    DEFAULT_CAPACITY = 10 # moderate capacity for all new queues

    def __init__ (self):
        '''Create an empty queue.'''
        self.data = [None]* ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0


    def __len__ (self):
        '''Return the number of elements in the queue.'''
        return self.size

    def is_empty(self):
        '''Return True if the queue is empty.'''
        return (self.size == 0)

    def __str__(self):
        return str(self.data)
    
    def first(self):
        '''Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty( ):
            raise Empty( 'Queue is empty' )
        return self.data[self.front]

    def dequeue(self):
        '''Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty( ):
            raise Empty( 'Queue is empty' )
        answer = self.data[self.front]
        self.data[self.front] = None # help garbage collection
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return answer

    def enqueue(self, e):
        '''Add an element to the back of queue.'''
        if self.size == len(self.data):
            self.resize(2*len(self.data)) # double the array size
        avail = (self.front + self.size) % len(self.data)
        #mod operator supports the circular action of the queue
        self.data[avail] = e
        self.size += 1

    def resize(self, cap): # we assume cap >= len(self)
        '''Resize to a new list of capacity >= len(self).'''
        old = self.data # keep track of existing list
        self.data = [None]*cap # allocate list with new capacity
        walk = self.front
        for k in range(self.size): # only consider existing elements
            self.data[k] = old[walk] # intentionally shift indices
            walk = (1 + walk) % len(old) # use old size as modulus
            self.front = 0

class Empty(Exception):
    '''Error attempting to access an element from an empty container.'''
    pass

if __name__ == "__main__":
    Q = ArrayQueue()    #create an object of array queue
    A = ArrayQueue()

    print(f'{A} initially empty!')
    A.enqueue(5)
    print(A)
    A.enqueue(3)
    print(A)
    A.dequeue()
    print(A)
    A.enqueue(2)
    print(A)
    A.enqueue(8)
    print(A)
    A.dequeue()
    print(A)
    A.dequeue()
    print(A)
    A.enqueue(9)
    print(A)
    A.enqueue(1)
    print(A)
    A.dequeue()
    print(A)
    A.enqueue(7)
    print(A)
    A.enqueue(6)
    print(A)
    A.dequeue()
    print(A)
    A.dequeue()
    print(A)
    A.enqueue(4)
    print(A)
    A.dequeue()
    print(A)
    A.dequeue()
    print(f'{A} the result')

    """
    4.  Suppose an initially empty queue Q has executed a total of 32 enqueue operations,
        10 first operations, and 15 dequeue operations, 5 of which raised Empty errors
        that were caught and ignored. What is the current size of Q? Add your answer to
        the end of the python file.
    
        Ths size of Q should be 32 - 10 = 22, assuming 5 failed dequeue operations. First
        operations would not impact size.
    """