# ProjectEulerProblem820.py

import unittest
import math
import sys

class test_ProjectEulerProblem820(unittest.TestCase):
    def nThDecimalDigitOf1ByX(self, n, x):
        if x == 1: return 0
        return ((10**n)//x) % 10
    def sumOfNthDigits(self, n):
        z = 0
        print()
        for k in range(1, n+1):
            nThDigit = self.nThDecimalDigitOf1ByX(n, k)
            print("S("+str(k)+") =", nThDigit)
            z = z + nThDigit
        return z
    def test_dnXCase1(self):
        self.assertTrue(
            self.nThDecimalDigitOf1ByX(7, 3) == 3
            )
    def test_dnXCase2(self):
        self.assertTrue(
            self.nThDecimalDigitOf1ByX(7, 2) == 0
            )
    def test_dnXCase3(self):
        self.assertTrue(
            self.nThDecimalDigitOf1ByX(7, 4) == 0
            )
    def test_dnXCase4(self):
        self.assertTrue(
            self.nThDecimalDigitOf1ByX(7, 5) == 0
            )
    def test_dnXCase5(self):
        self.assertTrue(
            self.nThDecimalDigitOf1ByX(7, 6) == 6
            )
    def test_dnXCase6(self):
        self.assertTrue(
            self.nThDecimalDigitOf1ByX(7, 7) == 1
            )
    def test_baseCaseFromProblem1(self):
        sys.set_int_max_str_digits(5000)
        self.assertTrue(
            self.sumOfNthDigits(7) == 10
            )
    def test_baseCaseFromProblem2(self):
        sys.set_int_max_str_digits(5000)
        self.assertTrue(
            self.sumOfNthDigits(100) == 418
            )
    def test_mainProblemDriver(self):
        sys.set_int_max_str_digits(10**9)
        print(
            self.sumOfNthDigits(10**7)
            )

if __name__ == "__main__":
    unittest.main()
