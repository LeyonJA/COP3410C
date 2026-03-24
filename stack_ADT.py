## COP3410
## Chapter 6: Stacks
## 11/02/2022



class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__ (self):
        '''Create an empty stack.'''
        self._data = [ ]                # nonpublic list instance

    def __len__ (self):
         '''Return the number of elements in the stack.'''
         return len(self._data)

    def is_empty(self):
         '''Return True if the stack is empty.'''
         return len(self._data) == 0

    def push(self, e):
         '''Add element e to the top of the stack.'''
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
        if self.is_empty( ):
          raise Empty( 'Stack is empty' )
        return self._data.pop( )        # remove last item from list

    def __str__(self):    #this method allows us to print the objects of stack class
        return(str(self._data))

class Empty(Exception):                 # Defines an Empty class as a trivial subclass of the Python Exception class.
    '''Error attempting to access an element from an empty container.'''
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


if __name__ == "__main__": 
    S = ArrayStack( ) # contents: [ ]
    S.push(5) # contents: [5]
    S.push(3) # contents: [5, 3]
    print(len(S)) # contents: [5, 3]; outputs 2
    print(S.pop( )) # contents: [5]; outputs 3
    print(S.is_empty()) # contents: [5]; outputs False
    print(S.pop( )) # contents: [ ]; outputs 5
    print(S.is_empty()) # contents: [ ]; outputs True
    S.push(7) # contents: [7]
    S.pop()
    S.push(9) # contents: [7, 9]
    print(S.top( )) # contents: [7, 9]; outputs 9
    S.push(4) # contents: [7, 9, 4]
    print(len(S)) # contents: [7, 9, 4]; outputs 3
    print(S.pop( )) # contents: [7, 9]; outputs 4
    S.push(6) # contents: [7, 9, 6]


    reverse_file('ReverseFile.txt')


    






