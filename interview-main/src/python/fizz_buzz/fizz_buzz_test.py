import unittest

from fizz_buzz import (
    fizzbuzz,
)

class FizzBuzzTest(unittest.TestCase):
    def test_returns_zero_for_input_of_zero(self):
        self.assertEqual(fizzbuzz(0), "zero")

    def test_returns_fizz_for_numbers_with_multiply_of_3(self):
        self.assertEqual(fizzbuzz(3), "fizz")
        self.assertEqual(fizzbuzz(18), "fizz")
        self.assertEqual(fizzbuzz(24), "fizz")
        self.assertEqual(fizzbuzz(48), "fizz")
        self.assertEqual(fizzbuzz(93), "fizz")
        self.assertEqual(fizzbuzz(1236), "fizz")

    def test_returns_buzz_for_numbers_with_multiply_of_5(self):
        self.assertEqual(fizzbuzz(5), "buzz")
        self.assertEqual(fizzbuzz(20), "buzz")
        self.assertEqual(fizzbuzz(50), "buzz")
        self.assertEqual(fizzbuzz(80), "buzz")
        self.assertEqual(fizzbuzz(200), "buzz")
        self.assertEqual(fizzbuzz(1000), "buzz")

    def test_returns_fizzbuzz_for_numbers_with_multiply_of_3_and_5(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")
        self.assertEqual(fizzbuzz(30), "fizzbuzz")
        self.assertEqual(fizzbuzz(45), "fizzbuzz")
        self.assertEqual(fizzbuzz(600), "fizzbuzz")
        self.assertEqual(fizzbuzz(1500), "fizzbuzz")
        self.assertEqual(fizzbuzz(6000), "fizzbuzz")

    def test_returns_input_number_for_other_input(self):
        self.assertEqual(fizzbuzz(4), 4)
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(17), 17)
        self.assertEqual(fizzbuzz(442), 442)
        self.assertEqual(fizzbuzz(13), 13)
        self.assertEqual(fizzbuzz(148), 148)
        self.assertEqual(fizzbuzz(202), 202)
