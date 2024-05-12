from Bank_and_info import*
from users import*
from admin import*

sonali_bank = Bank("Sonali Bank", 0)
print()
print("**** WELCOME TO SONALI BANK LIMITED ****")
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
            