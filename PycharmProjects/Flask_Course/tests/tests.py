from unittest import TestCase
from app import calc

class TestCalcMethods(TestCase):
    def test_calc(self):
        self.assertEqual(calc(1, 2), 4)

    def test_divide(self):
        self.assertEqual(divide(1, 2), 1)
        with self.assertRaises(TypeError):
            print(TypeError)

if __name__ == '__main__':
    tests = TestCalcMethods()
    tests.test_calc()
    tests.test_divide()