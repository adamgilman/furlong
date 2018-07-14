import unittest
from furlong import Furlong as f

class TestSimpleConversionTests(unittest.TestCase):
    def test_fixed_conversion_test(self):
        self.assertEqual( f(inches=12).asCentimeters(), 30.48 )

    def test_back_mapping_of_units(self):
        self.assertEqual( f(centimeters=30.48).asInches(), 12 )


class TestDyanmicFunctionNaming(unittest.TestCase):
    def setUp(self):
        test_conv = {
            'testbase'    : ('testconv', -1111),
        }
        f.conversion_table.update( test_conv )

    def test_dyanmic_function_exists(self):
        self.assertIsInstance( f(testbase=1), f )
        self.assertTrue( callable( f(testbase=1).asTestconv ) )
        self.assertEqual( f(testbase=2).asTestconv(), -2222 )

    def test_dyanamic_back_mapping(self):
        self.assertIsInstance( f(testconv=1), f )
        self.assertTrue( callable( f(testconv=1).asTestbase ) )
        self.assertEqual( f(testconv=1).asTestbase(), (1/-1111) )


