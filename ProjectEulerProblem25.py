# ProjectEulerProblem25.py

import unittest
import math
import sympy
import random
import sys

class test_ProjectEulerProblem25(unittest.TestCase):
	maxSpanFibonacciSeq = 0
	fibonacciMemoization = []
	def initDriver(self):
		self.fibonacciMemoization = [0 for k in range(self.maxSpanFibonacciSeq+1)]
		self.fibonacciMemoization[1] = 1
		self.fibonacciMemoization[2] = 1
		for k in range(3, self.maxSpanFibonacciSeq+1):
			self.fibonacciMemoization[k] = self.fibonacciMemoization[k-1] + self.fibonacciMemoization[k-2]
		self.assertTrue(True) 
	def digitCount(self, x):
		return math.ceil(math.log10(x))
	def test_DigitCountTestCase1(self):
		z = 11 + 88*random.random()
		self.assertTrue(self.digitCount(z) == 2)
	def test_DigitCountTestCase2(self):
		z = 101 + 898*random.random()
		self.assertTrue(self.digitCount(z) == 3)
	def test_DigitCountTestCase3(self):
		z = 1001 + 8998*random.random()
		self.assertTrue(self.digitCount(z) == 4)
	def test_DigitCountTestCase4(self):
		z = 10001 + 89998*random.random()
		self.assertTrue(self.digitCount(z) == 5)
	def test_FibNumberCase1(self):
		self.maxSpanFibonacciSeq = 10
		self.initDriver()
		self.assertTrue(self.fibonacciMemoization[1] == 1)
	def test_FibNumberCase2(self):
		self.maxSpanFibonacciSeq = 10
		self.initDriver()
		self.assertTrue(self.fibonacciMemoization[2] == 1)
	def test_FibNumberCase3(self):
		self.maxSpanFibonacciSeq = 10
		self.initDriver()
		self.assertTrue(self.fibonacciMemoization[3] == 2)
	def test_FibNumberCase4(self):
		self.maxSpanFibonacciSeq = 10
		self.initDriver()
		self.assertTrue(self.fibonacciMemoization[4] == 3)
	def test_FibNumberCase5(self):
		self.maxSpanFibonacciSeq = 10
		self.initDriver()
		self.assertTrue(self.fibonacciMemoization[5] == 5)
	def test_FibNumberCase6(self):
		self.maxSpanFibonacciSeq = 10
		self.initDriver()
		self.assertTrue(self.fibonacciMemoization[6] == 8)
	def test_FibNumberCase7(self):
		self.maxSpanFibonacciSeq = 10
		self.initDriver()
		self.assertTrue(self.fibonacciMemoization[7] == 13)
	def test_mainDriverFunction(self):
		self.maxSpanFibonacciSeq = 5000
		self.initDriver()
		for k in range(14, self.maxSpanFibonacciSeq+1):
			Fk = self.fibonacciMemoization[k]
			if self.digitCount(Fk) == 1000:
				print(
					"Minimum index of Fibonacci sequence",
					"with the first digit =", k
					)
				print(k,"th Fibonacci number =", Fk)
				break
		self.assertTrue(k == 4782)
if __name__ == "__main__":
	unittest.main()