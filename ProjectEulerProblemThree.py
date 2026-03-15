# ProjectEulerProblemThree.py

import unittest
import math


class test_ProjectEulerProblemThree(unittest.TestCase):
	def largestPrimeFactor(self, n):
		for p in range(n-1, 1, -1):
			if n%p == 0:
				flagPrimeFactor = True
				ceilSqrtP = math.ceil(math.sqrt(p))
				for k in range(ceilSqrtP, 1, -1):
					if p%k == 0:
						flagPrimeFactor = False
						break
				if flagPrimeFactor:
					break
		return p
	def test_TestCaseLPF1(self):
		self.assertTrue(self.largestPrimeFactor(4) == 2)
	def test_TestCaseLPF2(self):
		self.assertTrue(self.largestPrimeFactor(9) == 3)
	def test_TestCaseLPF3(self):
		self.assertTrue(self.largestPrimeFactor(16) == 2)
	def test_TestCaseLPF4(self):
		self.assertTrue(self.largestPrimeFactor(15) == 5)
	def test_TestCaseLPF5(self):
		self.assertTrue(self.largestPrimeFactor(69) == 23)
	def test_TestCaseLPF6(self):
		self.assertTrue(self.largestPrimeFactor(75) == 5)
	def test_TestCaseLPF7(self):
		self.assertTrue(self.largestPrimeFactor(81) == 3)
	def test_TestCaseLPF8(self):
		self.assertTrue(self.largestPrimeFactor(777) == 37)
	def test_TestCaseLPF9(self):
		self.assertTrue(self.largestPrimeFactor(1001) == 13)
	def test_TestCaseLPF10(self):
		self.assertTrue(self.largestPrimeFactor(13195) == 29)
	def test_TestCaseLPF11(self):
		print(self.largestPrimeFactor(600851475143))
		self.assertTrue(True)
if __name__ == "__main__":
	unittest.main()