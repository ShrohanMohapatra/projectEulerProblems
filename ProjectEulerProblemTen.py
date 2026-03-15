# ProjectEulerProblemTen.py

import unittest
import math

class test_ProjectEulerProblemTen(unittest.TestCase):
	def sumOfPrimesUntilN(self, n):
		if n < 2: return 0
		elif n == 2: return 2
		else:
			totalSum = 0
			prevPrime = 2
			while prevPrime < n:
				totalSum = totalSum + prevPrime
				x = prevPrime + 1
				if n == 2000000:
					print("Prime number p =", prevPrime)
				while True:
					flag = True
					ceilSqrtPrevP = math.ceil(math.sqrt(prevPrime))
					for k3 in range(2, ceilSqrtPrevP+1):
						if x % k3 == 0:
							flag = False
							break
					if flag: break
					else: x = x + 1
				prevPrime = x
			return totalSum
	def test_TestCase1SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(10) == 17)
	def test_TestCase2SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(12) == 28)
	def test_TestCase3SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(13) == 28)
	def test_TestCase4SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(14) == 41)
	def test_TestCase5SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(15) == 41)
	def test_TestCase6SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(18) == 58)
	def test_TestCase7SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(19) == 58)
	def test_TestCase8SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(20) == 77)
	def test_TestCase9SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(25) == 100)
	def test_TestCase10SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(30) == 129)
	def test_TestCase11SumPrimes(self):
		self.assertTrue(self.sumOfPrimesUntilN(2000000) == 142913828922)

if __name__ == "__main__":
	unittest.main()
