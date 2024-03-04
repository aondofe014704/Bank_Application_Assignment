import unittest

from bank_application.Bank import Bank
from bank_application.invalid_amount_exception import InvalidAmountError


class MyTestCase(unittest.TestCase):
    def test_to_register_customers_in_the_bank(self):
        bank = Bank("Greatness Overloaded Bank")
        bank.register_customer("first_name", "last_name", "6969")
        self.assertEqual(len(bank.list_of_accounts), 1)

    def test_to_deposit_money_in_the_bank(self):
        bank = Bank("Greatness Overloaded Bank")
        bank.register_customer("first_name", "last_name", "6969")
        bank.deposit(1, 5000)
        self.assertEqual(5000, bank.check_balance(1, "6969"))

    def test_that_we_deposit_twice_balance_increases(self):
        bank = Bank("Greatness Overloaded Bank")
        bank.register_customer("first_name", "last_name", "6969")
        bank.deposit(1, 700)
        bank.deposit(1, 700)
        self.assertEqual(1400, bank.check_balance(1, "6969"))

    def test_that_we_deposit_we_can_not_deposit_a_negative_balance_remains_unchanged(self):
        bank = Bank("Greatness Overloaded Bank")
        bank.register_customer("first_name", "last_name", "6969")
        self.assertRaises(InvalidAmountError, lambda: bank.deposit(1, -3000))
        self.assertEqual(0, bank.check_balance(1, "6969"))

    def test_that_we_can_withdraw_money_from_the_bank(self):
        bank = Bank("Greatness Overloaded Bank")
        bank.register_customer("first_name", "last_name", "6969")
        bank.deposit(1, 1200)
        bank.withdraw(1, 700, "6969")
        self.assertEqual(500, bank.check_balance(1, "6969"))
    def test_that_we_can_withdraw_twice_balance_decreases(self):
        bank = Bank("Greatness Overloaded Bank")
        bank.register_customer("first_name", "last_name", "6969")
        bank.deposit(1, 6000)
        bank.withdraw(1, 1000, "6969")
        bank.withdraw(1, 1000, "6969")
