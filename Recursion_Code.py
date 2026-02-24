"""
COP3410: Recursion, Recursive Alogirthms Intro
Instructor: Sareh Taebi
Date: 10/02/2024
"""

####### Let's write functions that can do a countdown from any number down to 1 ########

## Function1: Uses loops for countdown
def countdown_loop(i):
    while (i >= 1):
        print(i, sep= ' ')
        i-=1;

## Function2: Uses recursion for countdown
def countdown_recursive(i):
    print(i);
    if(i <= 1):
        return
    else:
        countdown_recursive(i-1)

## Factorial Function
def factorial(n):
    if n ==0:
        return 1                     #base case
    else:
        return n *factorial(n-1)     #recursive call to factorial


## Recursive binary search function 
def binary_search(data, target, low, high):
    """
    Return index if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False # interval is empty; no match else:
    mid = (low + high) // 2
    if target == data[mid]: # found a match 
        if target == data[mid -1]: #Trying to find the first occurence of target
            return binary_search(data, target, low, mid - 1) #This is to find the first occurence
        else:
            return mid
    elif target < data[mid]:
        # recur on the portion left of the middle
        return binary_search(data, target, low, mid - 1)
    else:
        # recur on the portion right of the middle
        return binary_search(data, target, mid + 1, high)

## Multiply elements of a list
def multiply_list(A,n):
    
    if n == 1:
        return A[0]
    elif n ==0:
        return 0
    elif A[n-1] == 0:
        return 0
    else:
        return multiply_list (A, n - 1) * A[n - 1]


## Add elements of a list
def linear_sum(S, n):
    """Return the sum
    of the first n numbers of sequence S."""
    if n == 0:
        return ''
    else:
        return linear_sum(S, n - 1) + S[n - 1]

## Reversing elements of an array
def reverse_array(A,start,stop):   #index: start and stop (len(A)-1)

    if start <stop:         #controls and forces to stop
        A[start],A[stop] = A[stop],A[start]  #swapping

        reverse_array(A,start+1, stop -1)   #recursion
    else:
        return

## Calculate x to the power of n
def calc_power(X,n):
    ''' computes x to the power of n , O(n)'''
    if n == 0:
        return 1
    else:
        return X * calc_power(X,n-1)

#How can I make the power algorithm more efficient? n//2 which results in O(logn)
#The current algorithm crashes with large values for n and x, it's O(n)
    
###BAD Fib Implementation ###
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

#Explore the good fib function! A fib function that calls itself only once!
#It's really bad for the function to call itself more than once. 

if __name__ == '__main__':

    datalist = "Hello Let's test Binary Search!"
    sortedlist = sorted(datalist)

    result = binary_search(sortedlist, 'X', 0, len(sortedlist)-1)
    print(result)


    #Testing linear sum
    list2 = list('hello')
    result2 = linear_sum(list2, len(list2))
    print('linear sum', result2)

    #Testing calc_power function
    print('calc power', calc_power(2,8))
    
    

