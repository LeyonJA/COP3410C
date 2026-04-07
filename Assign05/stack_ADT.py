"""
Coded by: Leyon Anderson
modifying the provided stack_ADT.py script to answer the following tasks.
4/06/2026
COP3410 Assignment #5

Stacks
1.  Take the stack_ADT file and use the ArrayStack implementation and modify
    it so that the stack has a limited capacity. The maximum capacity is set to maxlen
    elements, where maxlen is a parameter to the constructor. Pre-allocate a list with 
    length equal to the stack’s maximum capacity. If push is called when the stack is 
    at full capacity, throw a Full exception.

2.  In the same Python file, write a recursive method for removing all the elements
    from the stack. Test both features using a driver function to ensure that they 
    work properly.
"""

class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__ (self, maxlen):
        '''Create an empty stack.'''
        self._data = [ ]                # nonpublic list instance
        self._maxlen = maxlen

    def __len__ (self):
         '''Return the number of elements in the stack.'''
         return len(self._data)

    def is_empty(self):
         '''Return True if the stack is empty.'''
         return len(self._data) == 0

    def is_full(self):
         '''Return True if the stack is full.'''
         return len(self._data) == self._maxlen

    def push(self, e):
         '''Add element e to the top of the stack.'''
         try:
             if self.is_full():
                raise Full
         except Full:
             print('Stack is full!')
         else:
             self._data.append(e)           # new item stored at end of list

    def top(self):
         '''Return (but do not remove) the element at the top of the stack.
         Raise Empty exception if the stack is empty.
         '''
         if self.is_empty( ):
             raise Empty( 'Stack is empty' )
         return self._data[-1]          # the last item in the list

    def pop(self):
        '''Remove and return the element from the top of the stack (i.e., LIFO).

         Raise Empty exception if the stack is empty.
        '''
        try:        
            if self.is_empty( ):
                raise Empty
        except Empty:
            print('Stack is empty!')
            return self.top()
        else:
            return self._data.pop( )        # remove last item from list

    def __str__(self):    #this method allows us to print the objects of stack class
        return(str(self._data))

class Empty(Exception):                 # Defines an Empty class as a trivial subclass of the Python Exception class.
    '''Error attempting to access an element from an empty container.'''
    pass

class Full(Exception):                 # Defines an Empty class as a trivial subclass of the Python Exception class.
    '''Error attempting to increase stack past parameter maxlen.'''
    pass

def reverse_file(filename):
    '''Overwrite given file with its contents line-by-line reversed.'''
    print("reversefile executing")
    S = ArrayStack()
    original = open(filename)
    for line in original:
        for i in line:
            S.push(i) # we will re-insert newlines when writing
    original.close( )
    # now we overwrite with contents in LIFO order
    output = open(filename, 'w' ) # reopening file overwrites original
    while not S.is_empty( ):
        output.write(S.pop( )) # re-insert newline characters
    output.close( )

def empty_stack(S):
    '''Recursive function to empty the given stack.

    :param ArrayStack S: A stack.'''
    if len(S) == 0:
        return 
    else:
        S.pop()
        empty_stack(S)

def assign05():
    '''Create and test a stack. Then empty the stack with empty_stack() method.'''
    S = ArrayStack(5) # contents: [ ] and a maxlen of 5

    print(f'{S} initial stack is empty.')
    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    S.push(5)
    print(f'The size of the stack is: {len(S)}')
    S.push(6)
    print(f'The size of the stack is: {len(S)}')
    print(f'{S} current stack') # Verify that a stack was pre-loaded.

    empty_stack(S) # Call recursive function that will empty the stack.

    print(f'{S} after running empty_stack() method.') # Verify that the stack is indeed empty.
    print(f'The size of the stack is: {len(S)}')

if __name__ == "__main__": 
    assign05() # Call my driver function for assignment #5 questions 1-2.