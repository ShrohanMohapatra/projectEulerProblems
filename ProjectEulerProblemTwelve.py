# ProjectEulerProblemTwelve.py

import unittest
import math

class test_ProjectEulerProblemTwelve(unittest.TestCase):
	def listOfDivisors(self, n):
		returnList = []
		ceilSqrtN = math.ceil(math.sqrt(n))
		for k in range(1, ceilSqrtN+1):
			if n%k == 0:
				returnList.append(k)
				nBykIntegralDivide = n//k
				if nBykIntegralDivide not in returnList: returnList.append(nBykIntegralDivide)
		return returnList
	def nthTriangularNumber(self, n):
		return n*(n+1)//2
	def lowerCutoffTriangularNumber(self):
		cutOffNumDivisors = 500
		x = 0
		while True:
			x = x + 1
			z = self.nthTriangularNumber(x)
			divisorsList = self.listOfDivisors(z)
			numOfDivisors = len(divisorsList)
			print("-> Proceeded until z = ", z, "with", numOfDivisors, "divisors")
			if numOfDivisors > cutOffNumDivisors: break
		return z
	def test_TriangularNumberCase1(self):
		self.assertTrue(self.nthTriangularNumber(1) == 1)
	def test_TriangularNumberCase2(self):
		self.assertTrue(self.nthTriangularNumber(2) == 3)
	def test_TriangularNumberCase3(self):
		self.assertTrue(self.nthTriangularNumber(3) == 6)
	def test_TriangularNumberCase4(self):
		self.assertTrue(self.nthTriangularNumber(4) == 10)
	def test_TriangularNumberCase5(self):
		self.assertTrue(self.nthTriangularNumber(5) == 15)
	def test_TriangularNumberCase6(self):
		self.assertTrue(self.nthTriangularNumber(6) == 21)
	def test_TriangularNumberCase7(self):
		self.assertTrue(self.nthTriangularNumber(7) == 28)
	def test_testListOfDivisorsCase1(self):
		self.assertTrue(self.listOfDivisors(15) == [1, 15, 3, 5])
	def test_testListOfDivisorsCase1(self):
		self.assertTrue(self.listOfDivisors(16) == [1, 16, 2, 8, 4])
	def test_testListOfDivisorsCase2(self):
		self.assertTrue(self.listOfDivisors(27) == [1, 27, 3, 9])
	def test_testListOfDivisorsCase3(self):
		self.assertTrue(self.listOfDivisors(28) == [1, 28, 2, 14, 4, 7])
	def test_MainCase(self):
		print(self.lowerCutoffTriangularNumber())
		self.assertTrue(True)

if __name__ == "__main__":
	unittest.main()
