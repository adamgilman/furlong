import unittest
from furlong import Furlong as f

class TestSimpleConversionTests(unittest.TestCase):
    def test_fixed_conversion_test(self):
        self.assertEqual( f(inches=12).asCentimeters(), 30.48 )


class TestDyanmicFunctionNaming(unittest.TestCase):
    def test_dyanmic_function_exists(self):
        test_conv = {
            'testbase'    : ('testconv', -1111),
        }
        f.conversion_table.update( test_conv )
        self.assertIsInstance( f(testbase=1), f )
        self.assertTrue( callable( f(testbase=1).asTestconv ) )
        self.assertEqual( f(testbase=2).asTestconv(), -2222 )