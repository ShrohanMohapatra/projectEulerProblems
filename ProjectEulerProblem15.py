# ProjectEulerProblem15.py

import unittest
import math

class test_ProjectEulerProblem15(unittest.TestCase):
	def walkThroughGrid(self, n):
		W = [[0 for m in range(n+1)] for k in range(n+1)]
		for k in range(1, n+1):
			W[0][k] = 1
			W[k][0] = 1
		for k in range(1, n+1):
			for m in range(1, n+1):
				W[k][m] = W[k-1][m] + W[k][m-1]
		return W[n][n]
	def defaultTest1(self):
		self.assertTrue(True)
	def defaultTest2(self):
		self.assertFalse(False)
	def test_BaseCase2By2(self):
		self.assertTrue(self.walkThroughGrid(2) == 6)
	def test_BaseCase3By3(self):
		self.assertTrue(self.walkThroughGrid(3) == 20)
	def test_BaseCase4By4(self):
		self.assertTrue(self.walkThroughGrid(4) == 70)
	def test_BaseCase20By20(self):
		self.assertTrue(self.walkThroughGrid(20) == 137846528820)
if __name__ == "__main__":
	unittest.main()