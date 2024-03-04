from bank_application.Account import Account


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.list_of_accounts = []
        self.account_numbers = 1

    def register_customer(self, first_name, last_name, pin):
        full_name = first_name + " " + last_name
        account = Account(full_name, pin, self.account_numbers)
        self.list_of_accounts.append(account)
        self.account_numbers += 1
        return Account

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        account.deposit(amount)

    def find_account(self, account_number):
        for full_name in self.list_of_accounts:
            if full_name.number == account_number:
                return full_name

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        return account.check_balance(pin)

    def withdraw(self, number, amount, pin):
        account = self.find_account(number)
        account.withdraw(amount, pin)

