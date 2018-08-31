from devtools_02 import divide
import unittest


class TestDivision(unittest.TestCase):
    def setUp(self):
        self.num = 6

    def test_int_division(self):
        res = divide(self.num, 3)
        self.assertEqual(res, 2)

    def test_float_division(self):
        res = divide(self.num, 4)
        self.assertEqual(res, 1.5)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError) as err:
            res = divide(self.num, 0)
        self.assertEqual(str(err.exception), 'division by zero')

