# ProjectEulerProblem6Revisit2.py

import unittest

class test_ProjectEulerProblem6Revisit2(unittest.TestCase):
    def sumSquareDifference(self, n):
        return n*(n+1)*(3*n**2-n-2)//12
    def test_sumSqDiffV1(self):
        self.assertEqual(
            self.sumSquareDifference(10), 2640
            )
    def test_sumSqDiffV2(self):
        self.assertEqual(
            self.sumSquareDifference(15), 13160
            )
    def test_sumSqDiffV3(self):
        self.assertEqual(
            self.sumSquareDifference(100), 25164150
            )

if __name__ == "__main__":
    unittest.main()
