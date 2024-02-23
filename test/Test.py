import unittest
from test import Test


class TestIntegerListGeneration(unittest.TestCase):
    def setUp(self):
        self.test = Test()

    def test_collection_of_numbers(self):
        integer_numbers = self.test.collection_of_numbers()
        expected_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(integer_numbers, expected_numbers)

    def test_for_duplicates_elements(self):
        duplicated_list = self.test.duplicates_elements()
        expected_list = self.test.collection_of_numbers()
        self.assertEqual(duplicated_list, expected_list)


    def test_for_eliminates_duplicates(self):
        numbers = self.test.collection_of_numbers()
        eliminated_list = self.test.eliminates_duplicates(self.test.duplicates_elements())
        expected_list = numbers
        self.assertEqual(eliminated_list, expected_list)

    def test_addition_of_element(self):
        self.assertEqual(self.test.addition_of_element(list(range(1, 16))), 45)


    def test_for_addition_of_first_middle_last(self):
        self.assertEqual(self.test.addition_of_first_middle_last(list(range(1, 16))), 24)




