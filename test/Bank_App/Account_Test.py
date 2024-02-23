class Account_Test(unittest.TestCase):
    def setUp(self):
        self.account = Account("Omi ewa", 1234, 0, "987")

    def test_That_Account_can_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 50)

    def setUp(self):
        self.account = Account("Omi Ewa", 1344, 0, "987")

    def test_That_Can_Withdraw(self):
        self.account.deposit(1000)
        self.account.withdrawal(1000, "987")
        self.assertEqual(self.account.balanceChecker(500))