# ProjectEulerProblem28.py

import unittest

class test_ProjectEulerProblem28(unittest.TestCase):
	def spiralMatrixGen(self, k):
		# k is the number of layers
		# in the spiral matrix
		A = [[0 for b in range(2*k+1)] for a in range(2*k+1)]
		p = k
		q = k
		t = 1
		TwoKminusOneSq = (2*k+1)**2
		for s in range(1, TwoKminusOneSq+1):
			A[p][q] = s
			if s == (2*t-1)**2:
				t = t + 1
				q = q + 1
			elif (2*t-3)**2+1 <= s and s <= (2*t-3)**2+(2*t-3):
				p = p + 1
			elif (2*t-3)**2+(2*t-2) <= s and s <= (2*t-3)**2+(4*t-5):
				q = q - 1
			elif (2*t-3)**2+(4*t-4) <= s and s <= (2*t-3)**2+(6*t-7):
				p = p - 1
			elif (2*t-3)**2+(6*t-6) <= s and s <= (2*t-3)**2+(8*t-9):
				q = q + 1
		return A
	def sumOfCrossDiagonals(self, k):
		A = self.spiralMatrixGen(k)
		intendedSum = 0
		for m in range(2*k+1):
			intendedSum = intendedSum + A[m][m]
			intendedSum = intendedSum + A[m][2*k-m]
		intendedSum = intendedSum - A[k][k]
		return intendedSum
	def test_spiralMatrixCase1(self):
		B = [
			[7, 8, 9],
			[6, 1, 2],
			[5, 4, 3]
			]
		A = self.spiralMatrixGen(1)
		self.assertTrue(A == B)
	def test_spiralMatrixCase2(self):
		B = [
			[21, 22, 23, 24, 25],
			[20, 7, 8, 9, 10],
			[19, 6, 1, 2, 11],
			[18, 5, 4, 3, 12],
			[17, 16, 15, 14, 13]
			]
		A = self.spiralMatrixGen(2)
		self.assertTrue(A == B)
	def test_spiralMatrixCase3(self):
		B = [
			[43, 44, 45, 46, 47, 48, 49],
			[42, 21, 22, 23, 24, 25, 26],
			[41, 20, 7, 8, 9, 10, 27],
			[40, 19, 6, 1, 2, 11, 28],
			[39, 18, 5, 4, 3, 12, 29],
			[38, 17, 16, 15, 14, 13, 30],
			[37, 36, 35, 34, 33, 32, 31]
			]
		A = self.spiralMatrixGen(3)
		self.assertTrue(A == B)
	def test_sumOfDiagonalCase1(self):
		self.assertTrue(self.sumOfCrossDiagonals(1) == 25)
	def test_sumOfDiagonalCase2(self):
		self.assertTrue(self.sumOfCrossDiagonals(2) == 101)
	def test_sumOfDiagonalCase3(self):
		self.assertTrue(self.sumOfCrossDiagonals(3) == 261)
	def test_sumOfDiagonalCase4(self):
		# print(self.sumOfCrossDiagonals(500))
		self.assertTrue(self.sumOfCrossDiagonals(500) == 669171001)
if __name__ == "__main__":
	unittest.main()
