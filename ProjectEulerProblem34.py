# ProjectEulerProblem34.py

import unittest
import math

class test_ProjectEulerProblem34(unittest.TestCase):
	maxSpan = 100
	factorialMemoization = []
	def factorialDriver(self):
		self.factorialMemoization = [1 for k in range(self.maxSpan+1)]
		for k in range(1, self.maxSpan+1):
			self.factorialMemoization[k] = k*self.factorialMemoization[k-1]
	def sumOfDigits(self, z):
		strNum = str(z)
		lenStr = len(strNum)
		return sum([int(strNum[k]) for k in range(lenStr)])
	def sumOfFactorialOfDigits(self, z):
		strNum = str(z)
		lenStr = len(strNum)
		return sum([self.factorialMemoization[int(strNum[k])] for k in range(lenStr)])
	def test_factorialSetOfTests(self):
		self.maxSpan = 11
		self.factorialDriver()
		self.assertTrue(self.factorialMemoization[1] == 1)
		self.assertTrue(self.factorialMemoization[2] == 2)
		self.assertTrue(self.factorialMemoization[3] == 6)
		self.assertTrue(self.factorialMemoization[4] == 24)
		self.assertTrue(self.factorialMemoization[5] == 120)
		self.assertTrue(self.factorialMemoization[6] == 720)
		self.assertTrue(self.factorialMemoization[7] == 5040)
		self.assertTrue(self.factorialMemoization[8] == 40320)
		self.assertTrue(self.factorialMemoization[9] == 362880)
		self.assertTrue(self.factorialMemoization[10] == 3628800)
	def test_SumOfDigits(self):
		self.assertTrue(self.sumOfDigits(1234) == 10)
		self.assertTrue(self.sumOfDigits(43534) == 19)
		self.assertTrue(self.sumOfDigits(123541) == 16)
		self.assertTrue(self.sumOfDigits(145) == 10)
	def test_SumOfFactorialDigits(self):
		self.maxSpan = 11
		self.factorialDriver()
		self.assertTrue(self.sumOfFactorialOfDigits(1234) == 33)
		self.assertTrue(self.sumOfFactorialOfDigits(145) == 145)
		self.assertTrue(self.sumOfFactorialOfDigits(1657) == 5881)
	def test_MainDriver(self):
		self.maxSpan = 11
		maxSpanForFactorialDigSum = math.ceil(4.5*10**7) # 15000000
		self.factorialDriver()
		intendedSum = 0
		for k in range(3, maxSpanForFactorialDigSum+1):
			sumFactorialDigs = self.sumOfFactorialOfDigits(k)
			if k == sumFactorialDigs:
				print("Sum of factorial of digits equal to the number =", k)
				intendedSum += k
		print(intendedSum)
		self.assertTrue(True)

if __name__ == "__main__":
	unittest.main()
