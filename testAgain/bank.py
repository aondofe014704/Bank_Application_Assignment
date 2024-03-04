# from Account import Acccount
#
#
# class Bank:
#     def __init__(self, bank_name):
#         self.bank_name = bank_name
#         self.list_of_accounts = []
#         self.account_numbers = 1
#
#     def register_customer(self, first_name, last_name, account_pin):
#         full_name = first_name + last_name
#         account = Acccount(full_name, self.account_numbers, account_pin)
#         self.list_of_accounts.append(account)
#         self.account_numbers += 1
#         return Acccount
#
#     def remove_account(self, account_number, account_pin):
#         account = self.find_account(account_number)
#         if account.account_pin == account_pin:
#             self.list_of_accounts.remove(account)
#
#     def find_account(self, account_number: int) -> Acccount:
#         for account in self.list_of_accounts:
#             if account.account_number == account_number:
#                 self.account_numbers -= 1
#                 return account
