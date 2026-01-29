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
    
    def set_limit(self, limit):
        self._limit = limit
        
    def charge(self,purchase):
        '''
        A modification to charge method that would also decrement the limit
        '''

        if (purchase + self._balance) <= self._limit:
            self._balance += purchase
            return True    #The payment went through
        else:
            return False    #The payment didn't go through
        
    def make_payment(self,payment):
        '''Process customer payment that reduces balance.'''
        self._balance -= payment

    def __str__(self):
        """ Returns a string representation of self """
        return "\ncustomer: " + str(self._customer)+ "\nbank: " + str(self._bank) +"\naccount: " + str(self._account) +"\nlimit: " + str(self._limit) + "\nbalance: " + str(self._balance)


                

        

################### Inheritance ########################################

class PredatoryCreditCard(CreditCard):     #a child of the credit card class, it is inheriting all the methods and it's allowed to use all the instances from Credit Card
    ''' An extension to CreditCard that compounds interest and fees '''

    def __init__ (self, customer, bank, acnt, limit, apr):
     '''Create a new predatory credit card instance.
     The initial balance is zero.

     customer the name of the customer (e.g., John Bowman )
     bank the name of the bank (e.g., California Savings )
     acnt the acount identifier (e.g., 5391 0375 9387 5309 )
     limit credit limit (measured in dollars)
     apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
     '''
     
     #CreditCard. __init__ (self,customer, bank, acnt, limit) #use this technique or the one below
     super(). __init__ (customer, bank, acnt, limit) # call super constructor, this is the CreditCard initializer
     self._apr = apr

    def get_apr(self):
        ''' Returns the APR on a creditcard '''
        return self._apr

    
    def charge(self, price):
      ''' Charge given price to the card, assuming sufficient credit limit.
          Return True if charge was processed.
          Return False and assess 5 fee if charge is denied.
      '''
      success = super().charge(price)               # call inherited method
      if not success:
         self._balance += 5                          # assess penalty
      return success                                 # caller expects return value

     
    def process_month(self):
      '''Assess monthly interest on outstanding balance.'''
      if self._balance > 0:
       # if positive balance, convert APR to monthly multiplicative factor
          monthly_factor = pow(1 + self._apr, 1/12)   #1/12 power of (1+apr)
          self._balance = monthly_factor * self._balance

    def __str__(self):
        """ Returns a string representation of self """
        return "\ncustomer: " + str(self._customer) + "\nbank: " + str(self._bank) + "\naccount: " + str(self._account) + "\nlimit: " + str(self._limit) + "\nbalance: " + str(self._balance) + "\nAPR: " + str(self._apr)



 ############### Testing the class ########################################     
        
if __name__ == "__main__":       #uses test cases to test the class inside the same script file

##    Adams_card = CreditCard('Adam Best', 'United', '2300 3000 0000 0000', 1000)
##    print(Adams_card)
##    Adams_card.charge(10.50)
##    print(Adams_card)
##    success = Adams_card.charge(2000)
##    print("Did charge go through?", success)


   
   visa = PredatoryCreditCard('Sally Shoo', 'Vells','1234 5678 9012 3456', 5000,0.0825)   #calling the constructor
   
   print(visa)   # this shows the need for __str__ method
##   print('visa balance:', visa.get_balance())
##   print('visa limit:', visa.get_limit())
##   print('visa account:', visa.get_account())
   print('\nvisa charged $200:', visa.charge(200))
   visa.make_payment(100)
   visa.process_month()
   print(visa)
   print('\nvisa charged $5000:', visa.charge(5000)) 
   visa.process_month()
   print(visa)
   
 





    
