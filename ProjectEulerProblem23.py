# ProjectEulerProblem23.py

import unittest
import math

class test_ProjectEulerProblem23(unittest.TestCase):
	def listOfDivisors(self, x):
		returnList = []
		ceilSqrtX = math.ceil(math.sqrt(x))
		for k in range(1, ceilSqrtX+1):
			if x % k == 0:
				if k not in returnList:
					returnList.append(k)
				xByK = x//k
				if xByK not in returnList:
					returnList.append(xByK)
		returnList.sort()
		return returnList
	def sumOfProperDivisors(self, x):
		return sum(self.listOfDivisors(x)) - x
	def abundantNumberCheck(self, x):
		return self.sumOfProperDivisors(x) > x
	def mainDriver(self):
		maxSpan = 32000 # 29000 # 5*10**4 # 14063
		listOfAllowedPositiveInts = [k for k in range(math.ceil(2.5*maxSpan)+1)]
		abundantNumberList = []
		print("-"*40)
		for x in range(1, maxSpan+1):
			print(
					"x =", x,
					", self.sumOfProperDivisors(x) =",
					self.sumOfProperDivisors(x),
					"<>", self.abundantNumberCheck(x)
					)
			if self.abundantNumberCheck(x):
				abundantNumberList.append(x)
		print("-"*40)
		totalNumOfAbundants = len(abundantNumberList)
		for k in range(totalNumOfAbundants):
			print(">", abundantNumberList[k])
		print("-"*40)
		actualMaxSpan = 0
		for k in range(totalNumOfAbundants):
			for m in range(totalNumOfAbundants):
				sumKM = abundantNumberList[k] + abundantNumberList[m]
				actualMaxSpan = sumKM
				listOfAllowedPositiveInts[sumKM] = 0
		print("-"*40)
		for k in range(1, maxSpan+1):
			if listOfAllowedPositiveInts[k] != 0:
				print("-->", listOfAllowedPositiveInts[k])
		print("-"*40)
		return sum(listOfAllowedPositiveInts[24:maxSpan+1]) + 
	def test_DefaultTest1(self):
		self.assertTrue(True)
	def test_DefaultTest2(self):
		self.assertFalse(False)
	def test_divisorListCase1(self):
		self.assertTrue(self.listOfDivisors(12) == [1, 2, 3, 4, 6, 12])
	def test_divisorListCase2(self):
		self.assertTrue(
			self.listOfDivisors(64) == [1, 2, 4, 8, 16, 32, 64]
			)
	def test_divisorListCase3(self):
		self.assertTrue(
			self.listOfDivisors(28) == [1, 2, 4, 7, 14, 28]
			)
	def test_divisorListCase4(self):
		self.assertTrue(
			self.listOfDivisors(63) == [1, 3, 7, 9, 21, 63]
			)
	def test_divisorSumCase1(self):
		self.assertTrue(self.sumOfProperDivisors(12) == 16)
	def test_divisorSumCase2(self):
		self.assertTrue(self.sumOfProperDivisors(28) == 28)
	def test_divisorSumCase3(self):
		self.assertTrue(self.sumOfProperDivisors(27) == 13)
	def test_divisorSumCase4(self):
		self.assertTrue(self.sumOfProperDivisors(15) == 9)
	def test_divisorSumCase5(self):
		self.assertTrue(self.sumOfProperDivisors(63) == 41)
	def test_divisorSumCase4(self):
		self.assertFalse(self.abundantNumberCheck(27))
	def test_divisorSumCase5(self):
		self.assertTrue(self.abundantNumberCheck(12))
	def test_z_mainDriverFunction(self):
		sumOfAllowedPositiveInts = self.mainDriver()
		print(sumOfAllowedPositiveInts)
		self.assertTrue(True)

if __name__ == "__main__":
	unittest.main()
