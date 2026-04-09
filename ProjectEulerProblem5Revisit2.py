# ProjectEulerProblem5Revisit2.py

import unittest

class test_ProjectEulerProblem5Revisit2(unittest.TestCase):
    def gcdFinder(self, a, b):
        if a > b: return self.gcdFinder(b, a)
        elif b%a == 0: return a
        else: return self.gcdFinder(b%a, a)
    def lcmFinder(self, a, b):
        return a*b//self.gcdFinder(a, b)
    def evenDivisible(self, n):
        trackLCM = 2
        for k in range(3, n+1):
            trackLCM = self.lcmFinder(trackLCM, k)
        return trackLCM
    def test_evenDivisibleNumberBaseCase(self):
        self.assertTrue(self.evenDivisible(10) == 2520)
    def test_evenDivisibleNumberMainCase(self):
        self.assertTrue(self.evenDivisible(20) == 232792560)

if __name__ == "__main__":
    unittest.main()
