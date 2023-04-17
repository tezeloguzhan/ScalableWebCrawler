import unittest
from test_cache import TestCache
from test_parser import TestParser
class AllTests(unittest.TestCase):
    def test_cache(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCache)
        unittest.TextTestRunner(verbosity=1).run(suite)
        print("Cache Test Passed")


    def test_parser(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestParser)
        unittest.TextTestRunner(verbosity=2).run(suite)
        print("Parser Test Passed")

if __name__ == '__main__':
    unittest.main()
