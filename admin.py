from user import User

class Admin:
    def __init__(self):
        self.user_accounts = []

    def create_account(self, name, email, address, account_type):
        new_user = User(name, email, address, account_type)
        self.user_accounts.append(new_user)
        return new_user

    def delete_account(self, user):
        self.user_accounts.remove(user)

    def list_all_accounts(self):
        return self.user_accounts

    def total_balance(self):
        return sum(user.balance for user in self.user_accounts)

    def total_loan_amount(self):
        return sum(user.loan_taken for user in self.user_accounts)

    def toggle_loan_feature(self, status):
        # Implement logic to turn on/off loan feature
        pass
