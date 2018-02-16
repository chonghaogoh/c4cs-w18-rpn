import unittest
import rpm

class TestBasics(unittest.TestCase):
    def testAdd(self):
        result = rpm.calculate('1 1 +')
        self.assertEqual(2, result)
