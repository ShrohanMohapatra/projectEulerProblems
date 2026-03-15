# ProjectEulerProblem57.py

import unittest
import math

class test_ProjectEulerProblem57(unittest.TestCase):
	def convergentFraction(self, n):
		num, denom = 1, 1
		newNum, newDenom = 1, 1
		for k in range(n):
			newNum =  num + 2*denom
			newDenom = num + denom
			num = newNum
			denom = newDenom
		return [num, denom]
	def numOfDigits(self, m):
		return math.ceil(math.log10(m))
	def actualDriver(self):
		kMax = 1000
		num, denom = 1, 1
		newNum, newDenom = 1, 1
		count = 0
		for k in range(kMax):
			newNum =  num + 2*denom
			newDenom = num + denom
			num = newNum
			denom = newDenom
			if self.numOfDigits(num) > self.numOfDigits(denom):
				count += 1
		return count
	def defaultTest1(self):
		self.assertTrue(True)
	def defaultTest2(self):
		self.assertFalse(False)
	def test_convergentFractionTest1(self):
		expectedFraction = [3, 2]
		self.assertTrue(
			self.convergentFraction(1) == expectedFraction
			)
	def test_convergentFractionTest2(self):
		expectedFraction = [7, 5]
		self.assertTrue(
			self.convergentFraction(2) == expectedFraction
			)
	def test_convergentFractionTest3(self):
		expectedFraction = [17, 12]
		self.assertTrue(
			self.convergentFraction(3) == expectedFraction
			)
	def test_convergentFractionTest4(self):
		expectedFraction = [41, 29]
		self.assertTrue(
			self.convergentFraction(4) == expectedFraction
			)
	def test_convergentFractionTest5(self):
		expectedFraction = [99, 70]
		self.assertTrue(
			self.convergentFraction(5) == expectedFraction
			)
	def test_convergentFractionTest6(self):
		expectedFraction = [239, 169]
		self.assertTrue(
			self.convergentFraction(6) == expectedFraction
			)
	def test_convergentFractionTest7(self):
		expectedFraction = [577, 408]
		self.assertTrue(
			self.convergentFraction(7) == expectedFraction
			)
	def test_numOfDigitsCase1(self):
		self.assertTrue(self.numOfDigits(7) == 1)
	def test_numOfDigitsCase2(self):
		self.assertTrue(self.numOfDigits(87) == 2)
	def test_numOfDigitsCase3(self):
		self.assertTrue(self.numOfDigits(787) == 3)
	def test_numOfDigitsCase4(self):
		self.assertTrue(self.numOfDigits(7875) == 4)
	def test_numOfDigitsCase5(self):
		self.assertTrue(self.numOfDigits(78755) == 5)
	def test_numOfDigitsCase6(self):
		self.assertTrue(self.numOfDigits(787554) == 6)
	def test_numOfDigitsCase7(self):
		self.assertTrue(self.numOfDigits(7875754) == 7)
	def test_actualDriverTestCase(self):
		self.assertTrue(self.actualDriver() == 153)

if __name__ == "__main__":
	unittest.main()