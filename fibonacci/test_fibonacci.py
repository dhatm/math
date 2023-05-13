###########################################################################
# tests fibonacci implementations
###########################################################################


import unittest
from fibonacci import fibonacci_formula
from fibonacci import fibonacci_recursive
from fibonacci import fibonacci_iterative

class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci_formula(-5), 0)
        self.assertEqual(fibonacci_formula(0), 0)
        self.assertEqual(fibonacci_formula(1), 1)
        self.assertEqual(fibonacci_formula(2), 1)
        self.assertEqual(fibonacci_formula(5), 5)
        self.assertEqual(fibonacci_formula(10), 55)
        self.assertEqual(fibonacci_formula(20), 6765)

        self.assertEqual(fibonacci_recursive(-5), 0)
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci_recursive(10), 55)
        self.assertEqual(fibonacci_recursive(20), 6765)

        self.assertEqual(fibonacci_iterative(-5), 0)
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(1), 1)
        self.assertEqual(fibonacci_iterative(2), 1)
        self.assertEqual(fibonacci_iterative(5), 5)
        self.assertEqual(fibonacci_iterative(10), 55)
        self.assertEqual(fibonacci_iterative(20), 6765)


if __name__ == '__main__':
    unittest.main()



