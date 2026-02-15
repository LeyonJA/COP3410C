
"""
Coded by: Leyon Anderson
2/14/2026
Assignment #2

COP3410 - Classes and OOP
Modelling a credit card class - Parts taken from "Data Structures and Algorithms in Python"

Use the provided Python file and make extensions for more realistic behavior of a credit card class. Use the textbook for the following questions from chapter 2 (page 103):

R2-5 to R2-8
C-28 to C-30

R-2.5   Use the techniques of Section 1.7 to revise the charge and make payment
        methods of the CreditCard class to ensure that the caller sends a number
        as a parameter.
R-2.6   If the parameter to the make payment method of the CreditCard class
        were a negative number, that would have the effect of raising the balance
        on the account. Revise the implementation so that it raises a ValueError if
        a negative value is sent.
R-2.7   The CreditCard class of Section 2.3 initializes the balance of a new account 
        to zero. Modify that class so that a new account can be given a
        nonzero balance using an optional fifth parameter to the constructor. The
        four-parameter constructor syntax should continue to produce an account
        with zero balance.
R-2.8   Modify the declaration of the first for loop in the CreditCard tests, from
        Code Fragment 2.3, so that it will eventually cause exactly one of the three
        credit cards to go over its credit limit. Which credit card is it?


C-2.28  The PredatoryCreditCard class of Section 2.4.1 provides a process month
        method that models the completion of a monthly cycle. Modify the class
        so that once a customer has made ten calls to charge in the current month,
        each additional call to that function results in an additional $1 surcharge.
C-2.29  Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is 
        assigned a minimum monthly payment, as a percentage of the balance, and so that 
        a late fee is assessed if the customer does not subsequently pay that minimum 
        amount before the next monthly cycle.
C-2.30  At the close of Section 2.4.1, we suggest a model in which the CreditCard
        class supports a nonpublic method, set balance(b), that could be used
        by subclasses to affect a change to the balance, without directly accessing
        the balance data member. Implement such a model, revising both the
        CreditCard and PredatoryCreditCard classes accordingly
"""

################ Parent class of any credit card ##############################
class CreditCard:
    '''A consumer credit card.'''     #docstring, the first set of comments after the name of class is considered the help for that class. help(CreditCard)  

    def __init__ (self, customer, bank, acnt, limit, balance = 0):   #The constructor is the very first method
        '''
        Create a new credit card instance.

        The initial balance is zero.

        customer: the name of the customer (e.g., John Bowman )
        bank: the name of the bank (e.g., California Savings )
        acnt : the acount identifier (e.g., 5391 0375 9387 5309 )
        limit: credit limit (measured in dollars)

        R-2.7   The CreditCard class of Section 2.3 initializes the balance of a new account 
                to zero. Modify that class so that a new account can be given a
                nonzero balance using an optional fifth parameter to the constructor. The
                four-parameter constructor syntax should continue to produce an account
                with zero balance.
        '''
        self._customer = customer 
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance         # we start with a balance of zero, this is private, nobody can change it

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
    
    def _set_balance(self, balance):
        '''
        C-2.30  At the close of Section 2.4.1, we suggest a model in which the CreditCard
                class supports a nonpublic method, set balance(b), that could be used
                by subclasses to affect a change to the balance, without directly accessing
                the balance data member. Implement such a model, revising both the
                CreditCard and PredatoryCreditCard classes accordingly
        '''
        self._balance = balance
        
    def charge(self,purchase):
        '''
        A modification to charge method that would also decrement the limit

        R-2.5   Use the techniques of Section 1.7 to revise the charge and make payment
                methods of the CreditCard class to ensure that the caller sends a number
                as a parameter.
        '''
        if not isinstance(purchase, (int, float)):
            raise TypeError('parameter must be numeric')
        elif (purchase + self.get_balance()) <= self._limit:
            self._set_balance(self.get_balance() + purchase)
            return True    #The payment went through
        else:
            return False    #The payment didn't go through
        
    def make_payment(self,payment):
        '''
        Process customer payment that reduces balance.
            
        R-2.5   Use the techniques of Section 1.7 to revise the charge and make payment
                methods of the CreditCard class to ensure that the caller sends a number
                as a parameter.
        R-2.6   If the parameter to the make payment method of the CreditCard class
                were a negative number, that would have the effect of raising the balance
                on the account. Revise the implementation so that it raises a ValueError if
                a negative value is sent.

        '''        
        if not isinstance(payment, (int, float)):
            raise TypeError('parameter must be numeric')
        elif payment < 0:
            raise ValueError('parameter cannot be negative')
        else:
            self._set_balance(self.get_balance() - payment)

    def __str__(self):
        """ Returns a string representation of self """
        return "\ncustomer: " + str(self._customer)+ "\nbank: " + str(self._bank) +"\naccount: " + str(self._account) +"\nlimit: " + str(self._limit) + "\nbalance: " + str(self._balance)
    
################### Inheritance ########################################
class PredatoryCreditCard(CreditCard):     #a child of the credit card class, it is inheriting all the methods and it's allowed to use all the instances from Credit Card
    ''' An extension to CreditCard that compounds interest and fees '''

    def __init__ (self, customer, bank, acnt, limit, apr):
        '''
        Create a new predatory credit card instance.

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
        self._mTrans = 0 # number of monthly charges
        self._amtDue = {"Payments": 0, "Amt": 0} # Payment tracker

    def get_apr(self):
        ''' Returns the APR on a creditcard '''
        return self._apr
    
    def charge(self, price):
        ''' 
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied.

        C-2.28  The PredatoryCreditCard class of Section 2.4.1 provides a process month
                method that models the completion of a monthly cycle. Modify the class
                so that once a customer has made ten calls to charge in the current month,
                each additional call to that function results in an additional $1 surcharge.        
        '''
        self._mTrans += 1
        if self._mTrans > 10:
            super()._set_balance(super().get_balance() + 1)     # more than ten charges penalty

        success = super().charge(price)                         # call inherited method
        if not success:
           super()._set_balance(super().get_balance() + 5)      # assess penalty
        return success                                          # caller expects return value

    def process_month(self):
        '''
        Assess monthly interest on outstanding balance.

        C-2.29  Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is 
                assigned a minimum monthly payment, as a percentage of the balance, and so that 
                a late fee is assessed if the customer does not subsequently pay that minimum 
                amount before the next monthly cycle.
        '''
        if super().get_balance() > 0:
        # if positive balance, convert APR to monthly multiplicative factor
            if self._amtDue["Amt"] > 0:
                super()._set_balance(super().get_balance() + 15)          #apply late fee
                self._amtDue["Payments"] = 0

            monthly_factor = pow(1 + self._apr, 1/12)   #1/12 power of (1+apr)
            super()._set_balance(monthly_factor * super().get_balance())

    def make_payment(self, payment):
        '''
        C-2.29  Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is 
                assigned a minimum monthly payment, as a percentage of the balance, and so that 
                a late fee is assessed if the customer does not subsequently pay that minimum 
                amount before the next monthly cycle.
        '''
        if self._amtDue["Payments"] == 0:
            self._amtDue["Amt"] += super().get_balance() * 0.1
            self._amtDue["Payments"] += 1       

        if super().make_payment(payment):
            self._amtDue["Amt"] -= payment
            return True
        else:
            return False
    
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
##    print('visa balance:', visa.get_balance())
##    print('visa limit:', visa.get_limit())
##    print('visa account:', visa.get_account())
    print('\nvisa charged $200:', visa.charge(200))
    visa.make_payment(100)
    visa.process_month()
    print(visa)
    print('\nvisa charged $5000:', visa.charge(5000)) 
    visa.process_month()
    print(visa)

    '''
    R-2.8   Modify the declaration of the first for loop in the CreditCard tests, from
            Code Fragment 2.3, so that it will eventually cause exactly one of the three
            credit cards to go over its credit limit. Which credit card is it?
    '''
    print()
    print("=======Following card tried to go over thier limit=======")

    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))
    
    for val in range(1, 17):
        if not wallet[0].charge(10*val):
            print(wallet[0])
            break
        if not wallet[0].charge(15*val):
            print(wallet[1])
            break
        if not wallet[0].charge(20*val):
            print(wallet[2])
            break