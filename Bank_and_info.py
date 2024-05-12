from abc import ABC
import random


class Bank(ABC):
    def __init__(self, name, initial_balance) -> None:
        self.name = name
        self.bank_balance = initial_balance
        self.accounts = {}
        self.loan_feature = True
        self.bankrupt = False
        
        
class Bankinfo:
    def __init__(self, bank) -> None:
        self.bank = bank
        
    def create_account(self, name, email, password, address, account_type):
        account_number = random.randint(100000, 999999)
        self.bank.accounts[account_number] = {
            'name': name,
            'email': email,
            'password':password,
            'address': address,
            'account_type': account_type,
            'balance': 0,
            'transactions': [],
            'loan_taken': 0,
            'loan_amount': 0,
        }
        login_data = []
        login_data.append(account_number)
        login_data.append(self.bank.accounts[account_number]['password'])
        return login_data
    
    def delete_account(self, account_number):
        if account_number in self.bank.accounts:
            del self.bank.accounts[account_number]
            print("\nAccount Deleted Successfully")
        else:
            print("\nAccount Not Found")
            
    def get_all_account(self):
        i = 0
        if len(self.bank.accounts) == 0:
            print("No account Exist...!")
            return
        else: 
            for account_number, account_details in self.bank.accounts.items():
                i = i + 1
                print(f"***************** {i} NO PERSON ACCOUNT INFO ***************** \n")
                print("Account Number:", account_number)
                print("Account Details:")
                for key, value in account_details.items():
                    if key == 'transactions':
                        print("Transactions Details:")
                        for trans in value:
                            print(f"Type: {trans[0]}\tAmount=  {trans[1]}\tTransaction ID: {trans[2]}")
                        continue
                    print(key.upper() + ":", value)
                print()
        print(f"\nNumber of Existing Account is: {i}\n")
        
    def total_available_balance(self):
        return self.bank.bank_balance
    
    def total_loan_amount(self):
        total_loan = sum(account['loan_amount'] for account in self.bank.accounts.values())
        return total_loan
    
    def checking_for_loan(self, account_number):
        if self.bank.accounts[account_number]['loan_taken']==2:
            return False
        else:
            return True
        
    def security(self, account_number, password):
        if account_number in self.bank.accounts and self.bank.accounts[account_number]['password']==password:
            return True
        else:
            return False
            
