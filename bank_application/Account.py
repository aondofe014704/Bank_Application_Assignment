from bank_application.insufficient_funds_exception import InsufficientFundsException
from bank_application.invalid_amount_exception import InvalidAmountError
from bank_application.invalid_pin_exception import InvalidPinException


class Account:
    def __init__(self, name, pin, number):
        self.balance = 0
        self.name = name
        self.pin = pin
        self.number = number

    def check_balance(self, pin):
        if self.pin == pin:
            return self.balance
        raise InvalidPinException("Invalid pin")

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Invalid Amount")
        self.balance += amount

    def withdraw(self, amount, pin):
        #if self.balance > amount:
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient Funds")
        self.balance -= amount
