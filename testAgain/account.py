# class Acccount:
#     def __init__(self, account_name, account_pin,account_number):
#         self.name = account_name
#         self.account_pin = account_pin
#         self.account_balance = 0
#         self.account_number = account_number
#
#     def deposit(self, amount: int) -> None:
#         if amount > 0:
#             self.account_balance += amount
#         else:
#          raise ValueError("Obiakpor, Enter Invalid Amount")
#
#     def check_balance(self, password):
#         if self.account_pin == password:
#             return self.account_balance
#         raise ValueError("Obiakpor, Enter Correct Password Joor.")
#
#     def withdraw(self, balance, password):
#         if balance < self.account_balance:
#             self.account_balance -= balance
