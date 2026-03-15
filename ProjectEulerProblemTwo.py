# ProjectEulerProblemTwo.py

import unittest
import math

class test_ProjectEulerProblemTwo(unittest.TestCase):
	def fibonacciTerm(self, n):
		phi = (1 + math.sqrt(5))/2
		psi = (1 - math.sqrt(5))/2
		return math.floor((phi**(n+1) - psi**(n+1))/(phi - psi))
	def sumOfEvenValuedFibTerms(self, termSeq):
		if termSeq < 2: return 0
		else:
			x = 1
			sumOfTerms = 0
			fibTerm = 2
			while fibTerm <= termSeq:
				sumOfTerms += fibTerm
				x = x + 1
				fibTerm = self.fibonacciTerm(3*x-1)
			return sumOfTerms
	def test_FibTermCheck1(self):
		self.assertTrue(self.fibonacciTerm(1) == 1)
	def test_FibTermCheck2(self):
		self.assertTrue(self.fibonacciTerm(2) == 2)
	def test_FibTermCheck3(self):
		self.assertTrue(self.fibonacciTerm(3) == 3)
	def test_FibTermCheck4(self):
		self.assertTrue(self.fibonacciTerm(4) == 5)
	def test_FibTermCheck5(self):
		self.assertTrue(self.fibonacciTerm(5) == 8)
	def test_FibTermCheck6(self):
		self.assertTrue(self.fibonacciTerm(6) == 13)
	def test_SumOfIntendedTermsCase1(self):
		self.assertTrue(self.sumOfEvenValuedFibTerms(1) == 0)
	def test_SumOfIntendedTermsCase2(self):
		self.assertTrue(self.sumOfEvenValuedFibTerms(3) == 2)
	def test_SumOfIntendedTermsCase3(self):
		self.assertTrue(self.sumOfEvenValuedFibTerms(5) == 2)
	def test_SumOfIntendedTermsCase4(self):
		self.assertTrue(self.sumOfEvenValuedFibTerms(10) == 10)
	def test_SumOfIntendedTermsCase5(self):
		self.assertTrue(self.sumOfEvenValuedFibTerms(17) == 10)
	def test_SumOfIntendedTermsCase6(self):
		self.assertTrue(self.sumOfEvenValuedFibTerms(25) == 10)
	def test_SumOfIntendedTermsCase7(self):
		self.assertTrue(self.sumOfEvenValuedFibTerms(34) == 44)
	def test_SumOfIntendedTermsCase8(self):
		self.assertTrue(self.sumOfEvenValuedFibTerms(4000000) == 4613732)
if __name__ == "__main__":
	unittest.main()