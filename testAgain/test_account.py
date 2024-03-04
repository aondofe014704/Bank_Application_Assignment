# import unittest
#
# from Account import Acccount
#
#
# class MyTestCase(unittest.TestCase):
#     def test_for_deposit_invalid_amount_balance_remains_unchanged(self):
#         account = Acccount("account_name", "account_pin")
#         self.assertRaises(ValueError, lambda: account.deposit(-1_000))
#         self.assertEqual(0, account.check_balance("account_pin"))
#
#
#     def test_to_deposit_twice_balance_increase(self):
#         account = Acccount("account_name", "account_pin")
#         account.deposit(700)
#         account.deposit(2000)
#         self.assertEqual(2700, account.check_balance("account_pin"))
#
#     def test_for_no_negative_deposits(self):
#         account = Acccount("account_name", "69")
#         self.assertRaises(ValueError, lambda: account.deposit(-7000))
#         self.assertEqual(0, account.check_balance("69"))
#
#     def test_to_withdraw_balance_decrease(self):
#         account = Acccount("account_name", "account_pin")
#         account.deposit(9000)
#         account.withdraw(8000, "69")
#         self.assertEqual(1000, account.check_balance("account_pin"))
#
#     def test_to_withdraw_twice_balance_decreases(self):
#         account = Acccount("account_name", "69")
#         account.deposit(5000)
#         account.withdraw(2000, "69")
#         account.withdraw(1000, "69")
#         self.assertEqual(2000, account.check_balance("69"))
