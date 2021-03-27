import unittest
import run

class TestOps(unittest.TestCase):
    def test_double(self):
        self.assertEqual(run.double_me(1), 2)
        self.assertEqual(run.double_me(4), 8)

    def test_square(self):
        self.assertEqual(run.square_me(1.0), 1.0)
        self.assertEqual(run.square_me(4.0), 16.0)

if __name__ == "__main__":
    unittest.main()