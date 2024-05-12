from Bank_and_info import*

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

