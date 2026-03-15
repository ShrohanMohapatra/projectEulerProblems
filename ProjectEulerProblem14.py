# ProjectEulerProblem14.py

import unittest

class test_ProjectEulerProblem14(unittest.TestCase):
	def collatzSeqLengthChain(self, x):
		maxChain = -100
		numWithLongestChain = 3
		for y in range(3, x+1):
			z = y
			p = 0
			while z > 1:
				if z%2: z = 3*z+1
				else:  z = z//2
				p = p + 1
			if maxChain < p:
				maxChain = p
				numWithLongestChain = y
		return numWithLongestChain
	def collatzSeqLengthChainActualProblem(self):
		maxChain = -100
		numWithLongestChain = 3
		for y in range(3, 1000001):
			z = y
			p = 0
			while z > 1:
				if z%2: z = 3*z+1
				else:  z = z//2
				p = p + 1
			if maxChain < p:
				maxChain = p
				numWithLongestChain = y
				print(
					"Updated number with longest Collatz sequence chain = ", y
					)
		return numWithLongestChain
	def test_RegularCollatzSeqChainCase1(self):
		self.assertTrue(self.collatzSeqLengthChain(10) == 9)
	def test_RegularCollatzSeqChainCase2(self):
		self.assertTrue(self.collatzSeqLengthChain(20) == 18)
	def test_RegularCollatzSeqChainCase3(self):
		self.assertTrue(self.collatzSeqLengthChain(32) == 27)
	def test_RegularCollatzSeqChainCase4(self):
		self.assertTrue(self.collatzSeqLengthChain(33) == 27)
	def test_RegularCollatzSeqChainCase5(self):
		self.assertTrue(self.collatzSeqLengthChain(500) == 327)
	def test_RegularCollatzSeqChainCase7(self):
		print(self.collatzSeqLengthChainActualProblem())
		self.assertTrue(True)
	

if __name__ == "__main__":
	unittest.main()