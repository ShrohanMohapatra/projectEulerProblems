# ProjectEulerProblem30.py

import unittest
import math
import random

class test_digitFifthPowers(unittest.TestCase):
	def numOfDigits(self, x):
		return math.ceil(math.log10(x))
	def listOfDigits(self, x):
		numberOfDigits = self.numOfDigits(x)
		returnList = [0 for k in range(numberOfDigits)]
		z = x
		for k in range(numberOfDigits-1, -1, -1):
			returnList[k] = z%10
			z = z//10
		return returnList
	def driverDigitFourthPowers(self):
		maxSpan = 10**4
		returnList = []
		for x in range(2, maxSpan+1):
			numberOfDigits = self.numOfDigits(x)
			digitsOfX = self.listOfDigits(x)
			intendedSum = 0
			for k in range(numberOfDigits):
				intendedSum += digitsOfX[k]**4
			if intendedSum == x:
				returnList.append(x)
		return returnList
	def driverDigitFifthPowers(self):
		maxSpan = 2*10**6
		returnList = []
		for x in range(2, maxSpan+1):
			numberOfDigits = self.numOfDigits(x)
			digitsOfX = self.listOfDigits(x)
			intendedSum = 0
			for k in range(numberOfDigits):
				intendedSum += digitsOfX[k]**5
			if intendedSum == x:
				print("x = ", x)
				returnList.append(x)
		return returnList
	def defaultTest1(self):
		self.assertTrue(True)
	def defaultTest2(self):
		self.assertFalse(False)
	def test_numOfDigitsTestDriver1(self):
		x = random.randint(10, 99)
		self.assertTrue(self.numOfDigits(x) == 2)
	def test_numOfDigitsTestDriver2(self):
		x = random.randint(100, 999)
		self.assertTrue(self.numOfDigits(x) == 3)
	def test_numOfDigitsTestDriver3(self):
		x = random.randint(10**3, 10**4-1)
		self.assertTrue(self.numOfDigits(x) == 4)
	def test_numOfDigitsTestDriver4(self):
		x = random.randint(10**4, 10**5-1)
		self.assertTrue(self.numOfDigits(x) == 5)
	def test_listOfDigitsTestDriver1(self):
		x = 10234
		self.assertTrue(self.listOfDigits(x) == [1, 0, 2, 3, 4])
	def test_listOfDigitsTestDriver2(self):
		x = 102345
		self.assertTrue(self.listOfDigits(x) == [1, 0, 2, 3, 4, 5])
	def test_digitFourthPowersTest(self):
		expectedList = [1634, 8208, 9474]
		self.assertTrue(
			self.driverDigitFourthPowers() == expectedList
			)
	def test_digitFifthPowersTest(self):
		expectedList = self.driverDigitFifthPowers()
		print(expectedList)
		print(sum(expectedList))
		self.assertTrue(
			expectedList == [4150, 4151, 54748, 92727, 93084, 194979]
			)

if __name__ == "__main__":
	unittest.main()
