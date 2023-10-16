# Bank management system using python and SQLite 3
# Basic functions: create a account, withdraw money, deposit money, update account details, transfer money
# Written by Shubham Anand Jaiswal
# Terminal Run command: python main.py

import sqlite3
from random import randint

# Function to check if name entered is valid       
def valid_name(name):
    if name.isalpha() and not name.isspace() and len(name)>2:
        return True
    return False

# Create a Bank class
class Bank:
    print("WELCOME TO YOUR BANK")
    print("-------------------")
    def __init__(self):
        # Connect to database
        self.con = sqlite3.connect("bank.db")
        self.c = self.con.cursor()

    # Function to create account
    def create_account(self):
        self.con = sqlite3.connect("bank.db")
        self.c = self.con.cursor()
        # Query to Create bank table       
        self.c.execute("""create table if not exists bank
            (
                account_name text,
                acc_no integer,
                balance integer
            )""")
        
        # Get user Name
        fname = input("Enter Your First Name:- ").upper()
        lname = input("Enter Your Last Name:- ").upper()
        print("---------------------------------------")
        
        # Ensure valid name
        if valid_name(fname) and valid_name(lname):
            name = fname + ' ' + lname
            # Create random Id
            id = randint(10000000,99999999)
            # Initialize 0 amount as balance
            self.amount = 0
            
            # Query to insert new account into the bank table
            self.c.execute("insert into bank values(?,?,?)",(name,id,self.amount))
            print(f"Hello {name} Your Account got Created, Note your Your Account Number.")
            print(f"Your Account Number is:- {id}")
            print("---------------------------------------")
            self.con.commit()
            self.con.close()
            return
        # If invalid name, tell the user  
        else:
            print("Enter Valid Name, Try Again...!")
            
    # Function to read the account details
    def read_account(self):
        self.con = sqlite3.connect("bank.db")
        self.c = self.con.cursor()
        print("------------------------------")
        try:
            account_no = int(input("Enter the Account Number:- "))
        except ValueError:
            print("Please enter a valid number")
            return
            
        # To check if account exists
        not_found = True
        flag = False
        
        # Go through each row of bank table
        for db_holder_name, db_acc_no, db_balance in self.c.execute("select * from bank"):
            # If account number matches, ask further operations to perform
            if db_acc_no == account_no:
                flag = True
                not_found = False
                ac_bal = db_balance
                holder_name = db_holder_name
            # Stop the loop if account is found
            if flag:
                break
        
        # To keep displaying the menu   
        while flag:
            self.c.execute("select * from bank where acc_no = ?",(account_no,))
            holder_name, account_no, ac_bal = self.c.fetchone()
            
            if not not_found:
                print("------------------------------------------")
                print("(c)-Check Balance (d)-Deposit (w)-Withdraw (u)-Update Name (t)-Transfer (x)-Exit")
                operation = input("Enter any of the operation (c)/(d)/(w)/(u)/(t)/(x):- ").lower()
                print("------------------------------------------")
                print()
                
            # For deposit operation
            if flag and (operation == 'd'):
                dep = int(input("Enter the Amount to Deposit:- "))
                deposit = dep + ac_bal 
                self.c.execute("update bank set balance = ? where acc_no = ?",(deposit,account_no))
                self.con.commit()
                print(f"Amount Deposited {dep} ₹, Available Balance is {deposit} ₹")

            # For withdrawal operation
            elif flag and (operation == 'w'): 
                wit = int(input("Enter the Amount to Withdraw:- "))
                # Update balance if withdrawal amount is less than balance
                if ac_bal > 0 and ac_bal >= wit:
                    withdraw_bal = ac_bal - wit
                    self.c.execute("update bank set balance = ? where acc_no = ?",(withdraw_bal,account_no))
                    self.con.commit()
                    print(f"Withdraw {wit} ₹ done successfully...! Available balance {withdraw_bal} ₹")
                else:
                    print("Low Balance")
            
            # For Balance check operation
            elif flag and (operation == 'c'):
                print(f"Hello {holder_name}, Your Account Balance is {ac_bal} ₹")
            
            # For Account name update operation
            elif flag and (operation == 'u'):
                # get new name to update
                fname = input("Enter Your First Name:- ").upper()
                lname = input("Enter Your Last Name:- ").upper()
                
                # update name if valid
                if valid_name(fname) and valid_name(lname):
                    new_name = fname + ' ' + lname
                    self.c.execute("update bank set account_name = ? where acc_no = ?",(new_name,account_no))
                    self.con.commit()
                    print(f"Success! Your new name in account is {new_name}")
                else:
                    print("Enter Valid Name, Try Again...!")
                
            # For Money transfer operation
            elif flag and (operation == 't'):
                transfer_ac_no = int(input("Enter the Account Number for transfer:- "))
                transfer_amount = int(input("Enter the Amount to transfer:- "))
                
                # Transfer money if balance more than transfer amount
                if ac_bal > transfer_amount:
                    trans_success = False
                    for ac2_name, ac2_no, ac2_bal in self.c.execute("select * from bank"):
                        if ac2_no == transfer_ac_no:
                            self.c.execute("update bank set balance = ? where acc_no = ?",(ac2_bal + transfer_amount, ac2_no))
                            self.c.execute("update bank set balance = ? where acc_no = ?",(ac_bal - transfer_amount, account_no))
                            self.con.commit()
                            print(f"Transfer of {transfer_amount} ₹ done successfully...! Available balance {ac_bal - transfer_amount} ₹")
                            trans_success = True
                            break
                    if not trans_success:
                        print("Transfer unsuccessfull!!")
                else:
                    print("Insufficient balance")
              
            # For Exiting the menu     
            elif flag and (operation == 'x'):
                print("Thank for your patronage.")
                flag = False
        # If account is not in database, display a message
        if not_found:
            print("Invalid Account Number or Does not exist.")
            

# create object from Bank class            
bank = Bank()

# Keep showing the menu
menu_open = True
while menu_open:
    # Get user choice
    print("(c)-Create Account \n(o)-Open Account")
    choice = input("Enter your choice (c)/(o):- ").lower()
    
    # Call function based on choice
    if choice == 'c':
        bank.create_account()
    elif choice == 'o':
        bank.read_account()
    elif choice == 'x':
        menu_open = False
    else:
        print("Invalid choice")
