# ProjectEulerProblemSix.py

import unittest
import math

class test_ProjectEulerProblemSix(unittest.TestCase):
	def sumSquareDiff(self, n):
		return n*(n+1)*(3*n**2-n-2)//12
	def test_TestCase1(self):
		self.assertTrue(self.sumSquareDiff(10) == 2640)
	def test_TestCase2(self):
		self.assertTrue(self.sumSquareDiff(5) == 170)
	def test_TestCase3(self):
		self.assertTrue(self.sumSquareDiff(100) == 25164150)

if __name__ == "__main__":
	unittest.main()

