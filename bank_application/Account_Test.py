import unittest

from bank_application.Account import Account
from bank_application.insufficient_funds_exception import InsufficientFundsException
from bank_application.invalid_amount_exception import InvalidAmountError


class MyTestCase(unittest.TestCase):

    def test_that_account_is_empty_creation(self):
        account = Account("Jack Songu", "6969", 1)
        self.assertEqual(0, account.check_balance("6969"))

    def test_for_deposit_balance_increases(self):
        account = Account("James Brown", "6969", 1)
        account.deposit(5000)
        self.assertEqual(5000, account.check_balance("6969"))

    def test_for_that_we_cannot_deposit_negative_amount_balance_remain_unchanged(self):
        account = Account("Jay Jay", "6969", 1)
        with self.assertRaises(InvalidAmountError) as error:
            account.deposit(-1000)
        self.assertEqual(0, account.check_balance("6969"))

    def test_that_we_can_deposit_twice(self):
        account = Account("Kata Kata", "6969", 1)
        account.deposit(1000)
        account.deposit(1000)
        self.assertEqual(2000, account.check_balance("6969"))

    def test_that_we_can_not_deposit_zero_amount(self):
        account = Account("Mary Clark", "6969", "1")
        with self.assertRaises(InvalidAmountError):
            account.deposit(0)
        self.assertEqual(0, account.check_balance("6969"))

    def test_that_we_can_withdraw_balance_reduces(self):
        account = Account("Kelly Johnson", "6969", 1)
        account.deposit(5000)
        account.withdraw(3000, "6969")
        self.assertEqual(2000, account.check_balance("6969"))

    def test_for_no_withdraw_above_balance(self):
        account = Account("Angelle Dreams", "6969", 1)
        account.deposit(3000)
        self.assertRaises(InsufficientFundsException, lambda: account.withdraw(4000, "6969"))


if __name__ == '__main__':
    unittest.main()
