import unittest
from functools import partial
from devrandom import random, urandom, randint, choice

class TestRandom(unittest.TestCase):
    def test_number_of_chars(self):
        expected_len = 5
        actual_len = len(random(expected_len))
        self.assertEqual(expected_len, actual_len)

    def test_pseudo(self):
        self.assertRaises(NotImplementedError, partial(random, 1, path='/xxx/xxx/xxx'))
        expected_len = 5
        actual_len = len(random(expected_len, allow_pseudo=True, path='/xxx/xxx/xxx'))
        self.assertEqual(expected_len, actual_len)

        expected_len = 6
        actual_len = len(urandom(expected_len))
        self.assertEqual(expected_len, actual_len)

    def test_randint(self):
        low = 5
        high = 8
        for i in range(20):
            number = randint(low, high)
            self.assertTrue(low <= number <= high)

    def test_choice(self):
        self.assertEqual(choice([1]), 1)
        self.assertRaises(IndexError, choice, [])
