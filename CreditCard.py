'''
COP3410 - Classes and OOP
Modelling a credit card class - Parts taken from "Data Structures and Algorithms in Python"

'''


################ Parent class of any credit card ##############################

class CreditCard:
    '''A consumer credit card.'''     #docstring, the first set of comments after the name of class is considered the help for that class. help(CreditCard)  

    def __init__ (self, customer, bank, acnt, limit):   #The constructor is the very first method
        '''Create a new credit card instance.

        The initial balance is zero.

        customer: the name of the customer (e.g., John Bowman )
        bank: the name of the bank (e.g., California Savings )
        acnt : the acount identifier (e.g., 5391 0375 9387 5309 )
        limit: credit limit (measured in dollars)
        '''
        self._customer = customer 
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0         # we start with a balance of zero, this is private, nobody can change it

    def get_customer(self):   #The get functions are a must, they're called accessor functions (methods)
        '''Return name of the customer.'''
        return self._customer

    def get_bank(self):
        '''Return the bank s name.'''
        return self._bank

    def get_account(self):
        '''Return the card identifying number (typically stored as a string).'''
        return self._account

    def get_limit(self):
        '''Return current credit limit.'''
        return self._limit

    def get_balance(self):
        '''Return current balance.'''
        return self._balance
    
    
    def set_limit(self, limit):   # a setter would change the attribute values, we are allowing change to the limit
        self._limit = limit
        

    def charge(self,purchase):
        '''
        A modification to charge method that would also decrement the limit
        '''

        if (purchase + self._balance) <= self._limit:
            self._balance += purchase
            self._limit -= purchase
            return True 
        else:
            return False
        
    def make_payment(self,payment):
        '''Process customer payment that reduces balance.'''
        self._balance -= payment

    def __str__(self):
        """ Returns a string representation of self """
        return "\ncustomer: " + str(self._customer) + "\nbank: " + str(self._bank) + "\naccount: " + str(self._account) + "\nlimit: " + str(self._limit) + "\nbalance: " + str(self._balance)
        

        

############### Testing the class ########################################     
        
if __name__ == "__main__":  #uses test cases to test the class inside the same script file
    my_visa = CreditCard("Sareh Taebi", "CITI", '1234 5678 1234 5678', 15000)
    print(my_visa) #my visa information isn't printed becaues the print function cannot read objects with so many attbritues

    my_visa.charge(245.80)

    print(my_visa)

    my_visa.make_payment(57)

    print(my_visa)









    
