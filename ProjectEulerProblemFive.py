# ProjectEulerProblemFive.py

import unittest

class test_ProjectEulerProblemFive(unittest.TestCase):
	def gcdNumber(self, a, b):
		if a > b: return self.gcdNumber(b, a)
		elif a == b: return a
		elif b%a == 0: return a
		elif a == 1: return 1
		else: return self.gcdNumber(b%a, a)
	def lcmNumber(self, a, b):
		return a*b//self.gcdNumber(a, b)
	def smallestEvenlyDivisible(self, n):
		expectNum = self.lcmNumber(2, 3)
		for k in range(4, n+1):
			expectNum = self.lcmNumber(expectNum, k)
		return expectNum
	def test_TestCase1(self):
		self.assertTrue(self.smallestEvenlyDivisible(5) == 60)
	def test_TestCase2(self):
		self.assertTrue(self.smallestEvenlyDivisible(7) == 420)
	def test_TestCase3(self):
		self.assertTrue(self.smallestEvenlyDivisible(9) == 2520)
	def test_TestCase4(self):
		self.assertTrue(self.smallestEvenlyDivisible(10) == 2520)
	def test_TestCase5(self):
		self.assertTrue(self.smallestEvenlyDivisible(20) == 232792560)

if __name__ == "__main__":
	unittest.main()