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
    def testMul(self):
        result = rpn.calculate('2 2 *')
        self.assertEqual(4, result)
    def testDiv(self):
        result = rpn.calculate('8 4 /')
        self.assertEqual(2, result)
    def testMul2(self):
        result = rpn.calculate('8 3 * 2 *')
        self.assertEqual(48, result)
    def testDiv2(self):
        result = rpn.calculate('48 3 / 4 /')
        self.assertEqual(4, result)
    def testChain(self):
        result = rpn.calculate('2 2 + 1 - 3 *')
        self.assertEqual(9, result)
    def testPow(self):
        result = rpn.calculate('4 3 ^')
        self.assertEqual(64, result)
    def testPercent(self):
        result = rpn.calculate('0 72 + 5 %')
        self.assertEqual(75.6, result)
    def testIntDiv(self):
        result = rpn.calculate('5 2 .')
        self.assertEqual(2, result)
    def testFact(self):
        result = rpn.calculate('4 !')
        self.assertEqual(24, result)
    def testAnd(self):
        result = rpn.calculate('2 1 and')
        self.assertEqual(2 & 1, result)
    def testOr(self):
        result = rpn.calculate('4 3 or')
        self.assertEqual(4 | 3, result)
    def testNor(self):
        result = rpn.calculate('5 not')
        self.assertEqual(~5, result)