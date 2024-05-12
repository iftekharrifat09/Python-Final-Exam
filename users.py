import string
from Bank_and_info import*

class Users:
    def __init__(self, bank) -> None:
        self.bank = bank
        self.bankinfo = Bankinfo(bank)
        
    def create_account(self, name, email, password, address, account_type):
        return self.bankinfo.create_account(name, email, password, address, account_type)
    
    def see_account_details(self, account_number):
        print("\nHere is Your Account Details: ")
        for key,value in self.bank.accounts[account_number].items():
            if key == 'password':
                continue
            elif key == 'transactions':
                if  not self.bank.accounts[account_number]['transactions']:
                    print("There are no transactions yet")
                else:
                    print("Transactions Details:")
                    for trans in value:
                        print(f"Type: {trans[0]}\tAmount=  {trans[1]}\tTransaction ID: {trans[2]}")
                    print()
                    continue
            else:
                print(key.upper()+":", value)
                
                
            
    def transaction_history(self, account_number):
        for trans in self.bank.accounts[account_number]['transactions']:
            print(f"Type: {trans[0]}\tAmount=  {trans[1]}\tTransaction ID: {trans[2]}")
    
    def deposit_amount(self, account_number, amount):
        self.bank.accounts[account_number]['balance'] += amount
        self.bank.bank_balance += amount
        
        characters = string.ascii_letters + string.digits
        generated_transID = ''.join(random.choice(characters) for _ in range(10))
        trans_info = ('Deposit', +amount, generated_transID)
        self.bank.accounts[account_number]['transactions'].append(trans_info)
        
    def withdraw_amount(self, account_number, amount):
        if self.bank.bank_balance < self.bank.accounts[account_number]['balance']:
            print("The bank is Bankrupt")
        elif self.bank.bankrupt == True:
            print("The bank is Bankrupt")
        else:
            if self.bank.accounts[account_number]['balance'] < amount:
                print('You Have not enough amount to withdraw')
            else:
                print(f"Here is your amount {amount}")
                self.bank.accounts[account_number]['balance'] -= amount
                self.bank.bank_balance -= amount
                
                characters = string.ascii_letters + string.digits
                generated_transID = ''.join(random.choice(characters) for _ in range(10))
                trans_info = ('Withdraw', -amount, generated_transID)
                self.bank.accounts[account_number]['transactions'].append(trans_info)
            
    def check_available_balance(self, account_number):
        print(f"Your present balance is : { self.bank.accounts[account_number]['balance']}")
        
    def loan_taking(self, account_number):
        if self.bank.loan_feature == False:
            print("Loan Feature is Off")
        else:
            if self.bankinfo.checking_for_loan(account_number):
                print(f"Running {self.bank.accounts[account_number]['loan_taken']} Loan and Loan amount is : {self.bank.accounts[account_number]['loan_amount']}")
                while True:
                    print('1. Take a Loan\n2.Dont need any loan\n')
                    i = int(input('Enter Your Choice: '))
                    if i == 1:
                        amnt = int(input('Enter the amount to take: '))
                        self.bank.accounts[account_number]['loan_taken']+=1
                        self.bank.accounts[account_number]['loan_amount']+=amnt
                        self.bank.bank_balance -= amnt
                        break   
                    elif i == 2:
                        break
                    else:
                        print('You have Entered the wrong Command')
                        continue
            else:
                print("Loan Limit Exceeded")
            
    def transfer_amount(self, account_number):
        if self.bank.bank_balance < self.bank.accounts[account_number]['balance']:
            print("The bank is Bankrupt")
        elif self.bank.bankrupt == True:
            print("The bank is Bankrupt")
        else:
            friend_acc_no = int(input("Enter Your Friend account Number: "))
            if friend_acc_no in self.bank.accounts:
                amnt = int(input('Enter the amount to send: '))
                if amnt > self.bank.accounts[account_number]['balance']:
                    print("You do have that amount of money")
                else:
                    self.bank.accounts[friend_acc_no]['balance'] += amnt
                    self.bank.accounts[account_number]['balance'] -= amnt
                    print("Transfer Money Successfull\n")
                    
                    characters = string.ascii_letters + string.digits
                    generated_transID = ''.join(random.choice(characters) for _ in range(10))
                    trans_info_for_send = ('Send Money', -amnt, generated_transID)
                    trans_info_for_receive = ('Received', +amnt, generated_transID)
                    self.bank.accounts[account_number]['transactions'].append(trans_info_for_send)
                    self.bank.accounts[friend_acc_no]['transactions'].append(trans_info_for_receive)
            else:
                print("You Friend dont have a account in this bank")
