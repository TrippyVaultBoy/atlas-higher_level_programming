""" max_integer unittest """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer())

    def test_positive_numbers(self):

    def test_negative_numbers(self):

    def test_mixed_numbers(self):

    def test_duplicate_max(self):