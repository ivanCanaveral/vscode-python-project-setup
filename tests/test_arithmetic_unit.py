import unittest
from src.arithmetic import double_me, square_me, factorial


class TestDouble(unittest.TestCase):
    def test_double_positive(self):
        self.assertEqual(double_me(1), 2)
        self.assertEqual(double_me(4), 8)

    def test_double_negative(self):
        self.assertEqual(double_me(-1), -2)
        self.assertEqual(double_me(-4), -8)


class TestSquare(unittest.TestCase):
    def test_square_positive(self):
        self.assertEqual(square_me(1.0), 1.0)
        self.assertEqual(square_me(4.0), 16.0)

    def test_square_negative(self):
        self.assertEqual(square_me(-1.0), 1.0)
        self.assertEqual(square_me(-4.0), 16.0)


class TestFactorial(unittest.TestCase):

    def setUp(self):
        self.big_number: int = 100

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(4), 24)

    def test_factorial_negative(self):
        with self.assertRaises(TypeError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
