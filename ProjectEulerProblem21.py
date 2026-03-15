# ProjectEulerProblem21.py

import unittest
import math

class test_ProjectEulerProblem21(unittest.TestCase):
	def listOfDivisors(self, n):
		ceilSqrtN = math.ceil(math.sqrt(n))
		returnList = []
		for k in range(1, ceilSqrtN+1):
			if n % k == 0:
				nByk = n//k
				if k not in returnList: returnList.append(k)
				if nByk not in returnList: returnList.append(nByk)
		return returnList
	def sumOfDivisors(self, n):
		return sum(self.listOfDivisors(n)) - n
	def test_divisorTest1(self):
		expectedListOfDivisors = [1, 28, 2, 14, 4, 7]
		self.assertTrue(self.listOfDivisors(28) == expectedListOfDivisors)
	def test_divisorTest2(self):
		expectedListOfDivisors = [
			1, 72, 2, 36, 3, 24, 4, 18, 6, 12, 8, 9
			]
		self.assertTrue(self.listOfDivisors(72) == expectedListOfDivisors)
	def test_divisorTest3(self):
		expectedListOfDivisors = [
			1, 120, 2, 60, 3, 40, 4, 30, 5, 24, 6, 20, 8, 15, 10, 12
			]
		self.assertTrue(self.listOfDivisors(120) == expectedListOfDivisors)
	def test_divisorTest4(self):
		expectedListOfDivisors = [
			1, 84, 2, 42, 3, 28, 4, 21, 6, 14, 7, 12
			]
		self.assertTrue(self.listOfDivisors(84) == expectedListOfDivisors)
	def test_divisorTest5(self):
		expectedListOfDivisors = [
			1, 220, 2, 110, 4, 55, 5, 44, 10, 22, 11, 20
			]
		self.assertTrue(self.listOfDivisors(220) == expectedListOfDivisors)
	def test_sumOfDivisorTest1(self):
		self.assertTrue(self.sumOfDivisors(84) == 140)
	def test_sumOfDivisorTest2(self):
		self.assertTrue(self.sumOfDivisors(120) == 240)
	def test_sumOfDivisorTest3(self):
		self.assertTrue(self.sumOfDivisors(220) == 284)
	def test_sumOfDivisorTest4(self):
		self.assertTrue(self.sumOfDivisors(284) == 220)
	def test_sumOfDivisorTest4(self):
		self.assertTrue(self.sumOfDivisors(1) == 0)
	def test_finalDriver(self):
		maxSpan = 10000
		visitedList = [False for k in range(maxSpan+1)]
		amicableList = [k for k in range(maxSpan+1)]
		amicableList[0] = 0
		amicableList[1] = 0
		for k in range(2, maxSpan+1):
			if not(visitedList[k]):
				dk = self.sumOfDivisors(k)
				visitedList[k] = True
				if dk == 1:
					amicableList[k] = 0
				else:
					confirmDk = self.sumOfDivisors(dk)
					if k == confirmDk and k != dk:
						visitedList[dk] = True
						amicableList[dk] = k
						amicableList[k] = dk
					else: amicableList[k] = 0
		revisitList = [False for k in range(maxSpan+1)]
		for k in range(2, maxSpan+1):
			if not(revisitList[k]):
				revisitList[k] = True
				if amicableList[k] != 0:
					dk = amicableList[k]
					self.assertTrue(amicableList[dk] == k)
					revisitList[dk] = True
		self.assertTrue(sum(amicableList) == 31626)
if __name__ == "__main__":
	unittest.main()
