# ProjectEulerProblemThreeAttemptTwo.py

import unittest
import math


class test_ProjectEulerProblemThreeAttemptTwo(unittest.TestCase):
	def largestPrimeFactor(self, n):
		flagNprime = True
		ceilSqrtN = math.ceil(math.sqrt(n))
		for p in range(2, ceilSqrtN+1):
			if n%p == 0:
				if p == 2:
					flagNprime = False
					break
				else:
					flagPrimeFactor = True
					ceilSqrtP = math.ceil(math.sqrt(p))
					for k in range(2, ceilSqrtP+1):
						if p%k == 0:
							flagPrimeFactor = False
							break
					if flagPrimeFactor:
						flagNprime = False
						break
		if flagNprime: return n
		else:
			pOneFactor = p
			otherFactor = n//p
			pLargestOther = self.largestPrimeFactor(otherFactor)
			return max(pOneFactor, pLargestOther)
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
		self.assertTrue(self.largestPrimeFactor(600851475143) == 6857)
if __name__ == "__main__":
	unittest.main()