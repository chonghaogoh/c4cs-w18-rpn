import unittest
import rpn

class TestBasics(unittest.TestCase):
    def testAdd(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def testAdds(self):
        result = rpn.calculate('1 1 + 2 +')
        self.assertEqual(4, result)
    def testSub(self):
        result = rpn.calculate('5 2 -')
        self.assertEqual(3, result)
    def test_toomany(self):
        with self.assertRaises(TypeError):
            result = rpn.calculate('1 2 3 +')