#!/usr/bin/env python
# coding: utf-8

# # CREATING BANK ACCOUNT

# In[2]:


class Bank_Account: 
    def __init__(self): 
        self.balance=0
        self.name=str(input("enter your name"))
        print("enter name = " ,self.name)
        print("Hello!!! Welcome to the bank") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance so you can't withdraw it ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
        print("\n owner name=",self.name)
  # Driver code 
   
# creating an object of class 
s = Bank_Account() 
   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 

