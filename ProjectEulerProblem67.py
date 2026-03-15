# ProjectEulerProblem18.py

import unittest

class test_ProjectEulerProblem18(unittest.TestCase):
	def maxPathSum(self, A):
		Nx = len(A)
		B = [[0 for m in range(k+1)] for k in range(Nx)]
		B[0][0] = A[0][0]
		actualList = [B[0][0]]
		B[1][0] = A[1][0] + B[0][0]
		B[1][1] = A[1][1] + B[0][0]
		actualList = [B[1][0], B[1][1]]
		for k in range(2, Nx):
			B[k][0] = A[k][0] + max(B[k-1][0], B[k-1][1])
			B[k][k] = A[k][k] +  B[k-1][k-1]
			for m in range(1, k):
				B[k][m] = A[k][m] + max(B[k-1][m-1], B[k-1][m])
			actualList = [B[k][m] for m in range(k+1)]
		lastRow = [B[Nx-1][k] for k in range(Nx)]
		return max(lastRow)
	def test_backUpTestSuiteV1(self):
		A = [
			[1],
			[2, 3],
			[4, 6, 5],
			[7, 9, 10, 8],
			[11, 12, 13, 14, 15]
			]
		self.assertTrue(self.maxPathSum(A) == 34)
	def test_backUpTestSuiteV2(self):
		A = [
			[7], [8, 9], [7, 6, 5], [3, 4, 6, 7]
			]
		self.assertTrue(self.maxPathSum(A) == 28)
	def test_backUpTestSuiteV3(self):
		A = [
			[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],
			[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]
			]
		self.assertTrue(self.maxPathSum(A) == 8)
	def test_backUpTestSuiteV4(self):
		A = [
			[8],
			[6, 7],
			[10, 8, 9],
			[5, 6, 7, 8],
			[7, 8, 9, 2, 3],
			[5, 6, 7, 4, 5, 3],
			[10, 11, 5, 7, 3, 4, 9]
			]
		self.assertTrue(self.maxPathSum(A) == 56)
	def test_backUpTestSuiteV5(self):
		A = [
			[3],
			[7, 4],
			[2, 4, 6],
			[8, 5, 9, 3]
			]
		self.assertTrue(self.maxPathSum(A) == 23)
	def test_backUpTestSuiteV6(self):
		A = [
			[75],
			[95, 64],
			[17, 47, 82],
			[18, 35, 87, 10],
			[20, 4, 82, 47, 65]
			]
		self.assertTrue(self.maxPathSum(A) == 390)
	def test_mainDriver(self):
		fileHandle = open("0067_triangle.txt", "r")
		listOfLines = fileHandle.readlines()
		Nx = len(listOfLines)
		A = [[0 for m in range(Nx)] for k in range(Nx)]
		print()
		for k in range(Nx):
			strLines = listOfLines[k]
			strListOfNumbers = strLines.split()
			actualList = [0 for m in range(k+1)]
			for m in range(k+1):
				A[k][m] = int(strListOfNumbers[m])
				actualList[m] = A[k][m]
			print("A["+str(k+1)+"][:] =", actualList)
		print("Maximum path number =", self.maxPathSum(A))
		self.assertTrue(True)
		fileHandle.close()

if __name__ == "__main__":
	unittest.main()