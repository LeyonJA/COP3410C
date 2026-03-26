# Implement a Queue data structure using a Python list

class Queue(object):
   def __init__(self, size):             # Constructor
      self.__maxSize = size              # Size of [circular] array
      self.__que = [None] * size         # Queue stored as a list
      self.__front = 1                   # Empty Queue has front 1
      self.__rear = 0                    # after rear and
      self.__nItems = 0                  # No items in queue
 
   def enqueue(self, item):               # Insert item at rear of queue
      if self.is_full():                  # if not full
         raise Exception("Queue overflow")
      self.__rear += 1                   # Rear moves one to the right
      if self.__rear == self.__maxSize:  # Wrap around circular array
         self.__rear = 0
      self.__que[self.__rear] = item     # Store item at rear
      self.__nItems += 1
      return True
 
   def dequeue(self):                     # Remove front item of queue
      if self.is_empty():                 # and return it, if not empty
         raise Exception("Queue underflow")
      front = self.__que[self.__front]   # get the value at front
      self.__que[self.__front] = None    # Remove item reference
      self.__front += 1                  # front moves one to the right
      if self.__front == self.__maxSize: # Wrap around circular arr.
         self.__front = 0
      self.__nItems -= 1
      return front
 
   def first(self):                       # Return frontmost item
      return None if self.is_empty() else self.__que[self.__front]
 
   def is_empty(self): return self.__nItems == 0
 
   def is_full(self): return self.__nItems == self.__maxSize
 
   def __len__(self): return self.__nItems
 
##   def __str__(self):                    # Convert queue to string
##      ans = "["                          # Start with left bracket
##      for i in range(self.__nItems):     # Loop through current items
##         if len(ans) > 1:                # Except next to left bracket,
##            ans += ", "                  # separate items with comma
##         j = i + self.__front            # Offset from front
##         if j >= self.__maxSize:         # Wrap around circular array
##            j -= self.__maxSize
##         ans += str(self.__que[j])       # Add string form of item
##      ans += "]"                         # Close with right bracket
##      return ans


   def __str__(self):
      return(str(self.__que))

if __name__ == "__main__":
    Q= Queue(20)    #create an object of array queue
    Q.enqueue(5)
    Q.dequeue()
    print(Q.is_empty())
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(7)
    Q.enqueue(8)
    Q.enqueue(9)
    Q.enqueue(10)
    Q.enqueue(11)
    Q.enqueue(12)
    print(len(Q))
    print(Q)
    print(Q.first())
    


