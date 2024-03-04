# import unittest
#
# from Bank import Bank
#
#
# class MyTestCase(unittest.TestCase):
#     def test_to_register_customers_in_the_bank(self):
#         bank = Bank("Jack Songu's Bank")
#         bank.register_customer("first_name", "last_name", "account_pin")
#         self.assertEqual(len(bank.list_of_accounts), 1)
#     def test_to_remove_customers_account_in_the_bank(self):
#         bank = Bank("Jack Songu's Bank")
#         bank.register_customer("first_name", "last_name", "account_pin")
#         self.assertEqual(1, bank.remove_account(1, "account_pin"))
#     def test_to_find_account_in_the_bank(self):
#         bank = Bank("Jack Songu's Bank")
#         bank.find_account(1)
#         self.assertEqual(len(bank.list_of_accounts), 0)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     #def test_to_remove_account_in_the_bank(self):
#      #   bank = Bank("Jack Songu's Bank")
#       #  bank.remove_account(1, "account_pin")
#
