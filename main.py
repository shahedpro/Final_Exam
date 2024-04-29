from user import User, generate_account_number
from admin import Admin

def main():
    admin = Admin()
    while True:
        print("Welcome to the Bank Management System")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # User login
            user_menu(admin)
        elif choice == '2':
            # Admin login
            admin_menu(admin)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(admin):
    print("User Login")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    account_type = input("Enter account type (Savings/Current): ")

    user = admin.create_account(name, email, address, account_type)

    while True:
        print("\nUser Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Take Loan")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            user.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            user.withdraw(amount)
        elif choice == '3':
            recipient_name = input("Enter recipient's name: ")
            recipient = find_user_by_name(admin, recipient_name)
            if recipient:
                amount = float(input("Enter transfer amount: "))
                user.transfer(recipient, amount)
            else:
                print("Recipient not found")
        elif choice == '4':
            print("Current Balance:", user.check_balance())
        elif choice == '5':
            print("Transaction History:", user.check_transaction_history())
        elif choice == '6':
            if user.loan_taken < 2:
                amount = float(input("Enter loan amount: "))
                user.take_loan(amount)
            else:
                print("You've already taken the maximum number of loans")
        elif choice == '7':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")

def find_user_by_name(admin, name):
    for user in admin.list_all_accounts():
        if user.name == name:
            return user
    return None

def admin_menu(admin):
    print("Admin Login")
    # Implement admin login/authentication logic here

    while True:
        print("\nAdmin Menu")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. List All Accounts")
        print("4. Check Total Balance")
        print("5. Check Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter account type (Savings/Current): ")
            admin.create_account(name, email, address, account_type)
        elif choice == '2':
            name = input("Enter user's name to delete account: ")
            user = find_user_by_name(admin, name)
            if user:
                admin.delete_account(user)
                print("Account deleted successfully.")
            else:
                print("User not found")
        elif choice == '3':
            print("List of All Accounts:")
            for user in admin.list_all_accounts():
                print(user.name, "-", user.account_number)
        elif choice == '4':
            print("Total Balance:", admin.total_balance())
        elif choice == '5':
            print("Total Loan Amount:", admin.total_loan_amount())
        elif choice == '6':
            status = input("Enter 'on' to enable loan feature or 'off' to disable: ")
            admin.toggle_loan_feature(status)
        elif choice == '7':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
