# ProjectEulerProblemOne.py

import unittest

class test_ProjectEulerProblemOne(unittest.TestCase):
	def sumOfMultiplesOfThreeOrFive(self, x):
		# I am assuming strictly positive integral x
		intendedSum = 0
		for k in range(1, x):
			if k%3 == 0 or k%5 == 0:
				intendedSum += k
		return intendedSum
	def test_TestCase1(self):
		self.assertTrue(self.sumOfMultiplesOfThreeOrFive(10) == 23)
	def test_TestCase2(self):
		self.assertTrue(self.sumOfMultiplesOfThreeOrFive(20) == 78)
	def test_TestCase3(self):
		self.assertTrue(self.sumOfMultiplesOfThreeOrFive(1000) == 233168)

if __name__ == "__main__":
	unittest.main()