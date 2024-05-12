from abc import ABC
import random
import string

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
            
class Admin():
    def __init__(self, bank) -> None:
        self.bankinfo = Bankinfo(bank)
        self.bank = bank
    
    #admin can create an account for user
    def create_account_for_user(self, name, email, password, address, account_type):
        return self.bankinfo.create_account(name, email, password, address, account_type)
    
    def delete_user_account(self, account_number):
       self.bankinfo.delete_account(account_number)
    
    def see_all_users(self):
        print("1. hello")
        self.bankinfo.get_all_account()
    
    def check_bank_available_balance(self):
        print(f"Bank Present Balance Is: {self.bankinfo.total_available_balance()}")
    
    def check_total_loan_in_bank(self):
        print(f"Total Loan is: {self.bankinfo.total_loan_amount()}")
    
    def feature_setting(self):
        while(True):
            print("\n1.Trun ON/OFF Loan Feature\n2.Declare Bankrupt\n3.Exit...")
            i = int(input("Enter Your Choice: "))
            if i==1:
                print("\n1. ON\n2. OFF\n3.Exit Option")
                while(True):
                    j = int(input("Select One: "))
                    if j==1:
                        self.bank.loan_feature = True
                        print("Setting Update SuccessFul\n")
                        break
                    elif j==2:
                        self.bank.loan_feature = False
                        print("Setting Update SuccessFul\n")
                        break
                    elif j==3:
                        break
                    else:
                        print("Wrong Selection. Try Again\n")
                        continue
            elif i==2:
                print("\n1. ON\n2. OFF\n3.Exit Option")
                while(True):
                    j = int(input("Select One: "))
                    if j==1:
                        self.bank.bankrupt = True
                        print("Setting Update SuccessFul\n")
                        break
                    elif j==2:
                        self.bank.bankrupt = False
                        print("Setting Update SuccessFul\n")
                        break
                    elif j==3:
                        break
                    else:
                        print("Wrong Selection. Try Again\n")
                        continue
            elif i==3:
                break
            else:
                print("Wrong Choice. Try Again\n")
                continue

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
                print(f'Running {self.bank.accounts[account_number]['loan_taken']} Loan and Loan amount is : {self.bank.accounts[account_number]['loan_amount']}')
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

sonali_bank = Bank("Sonali Bank Limited", 0)
print()
print(f"**** WELCOME TO {sonali_bank.name} ****")
while True:
    print("1. Admin\n2. User\n3. Exit....")
    choice = int(input("Enter As: "))
    
    if choice==1:
        admin = Admin(sonali_bank)
        while True:
            print("1. Create Account For User\n2. Delete User Account\n3. All User Account List\n4. Available Balance of Bank")
            print("5. Total Loan Amount\n6. Feature Setting\n7. Insert Money In the Bank\n8. Exit...")
            cmnd = int(input("Enter Your Choice: "))
            if cmnd == 1:
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                password = input("Enter a Password: ")
                address = input("Enter Address: ")
                account_type = input("Enter Account Type: ")
                acnt_info = admin.create_account_for_user(name, email, password, address, account_type)
                print(f"\nYour Account No: {acnt_info[0]} Password Is: {acnt_info[1]}\n")
            elif cmnd == 2:
                acNo = int(input("Enter User Account Number: "))
                admin.delete_user_account(acNo)
                print()
            elif cmnd == 3:
                admin.see_all_users()
                print()
            elif cmnd == 4:
                admin.check_bank_available_balance()
                print()
            elif cmnd == 5:
                admin.check_total_loan_in_bank()
                print()
            elif cmnd == 6:
                admin.feature_setting()
                print()
            elif cmnd == 7:
                taka = int(input("Enter Money to Insert: "))
                sonali_bank.bank_balance = taka
                print("Money Insert Successfull")
                print()
            elif cmnd == 8:
                break
            else:
                print("You Have Entered Wrong Command. Try Again")
                print()
                continue
    elif choice == 2:
        user = Users(sonali_bank)
        while True:
            print("1. Create Account\n2. Log In\n3. Exit..")
            take = int(input("Enter your Desire: "))
            if take == 1:
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                password = input("Enter a Password: ")
                address = input("Enter Address: ")
                account_type = input("Enter Account Type: ")
                acnt_info = user.create_account(name, email, password, address, account_type)
                print(f"\nYour Account No: {acnt_info[0]} Password Is: {acnt_info[1]}\n")
                print()
            elif take == 2:
                acno = int(input("Enter Your Account Number: "))
                pas = input("Enter Your Password: ")
                print()
                if Bankinfo(sonali_bank).security(acno, pas) == True:
                    print("Welcome To Your Account")
                    while True:
                        print("1. Deposit Amount\n2. Withdraw Amount\n3. Check Balance\n4. Transaction History")
                        print("5. Take Loan\n6. Transfer Money\n7. Account Details\n8. Exit...")
                        command = int(input("Enter Your Command: "))
                        if command == 1:
                            amnt = abs(int(input("Enter an Amount: ")))
                            user.deposit_amount(acno, amnt)
                            print()
                        elif command == 2:
                            amnt = int(input("Enter an Amount: "))
                            user.withdraw_amount(acno, amnt)
                            print()
                        elif command == 3:
                            user.check_available_balance(acno)
                            print()
                        elif command == 4:
                            user.transaction_history(acno)
                            print()
                        elif command == 5:
                            user.loan_taking(acno)
                            print()
                        elif command == 6:
                            user.transfer_amount(acno)
                            print()
                        elif command == 7:
                            user.see_account_details(acno)
                            print()
                        elif command == 8:
                            break
                        else:
                            print("You Have Entered Wrong Command. Try Again")
                            print()
                            continue
                else:
                    print("Invalid Entry")
                    print()
            elif take == 3:
                break
            else:
                print("Wrong Selection. Try Again")
                print()
                continue
    else:
        break
            