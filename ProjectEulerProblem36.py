# ProjectEulerProblem36.py

import unittest

class test_ProjectEulerProblem36(unittest.TestCase):
	def decimalToBinary(self, x):
		n = x
		listOfBits = []
		while n > 0:
			listOfBits.append(n%2)
			n = n // 2
		numOfBits = len(listOfBits)
		binNo = 0
		for k in range(numOfBits-1, -1, -1):
			binNo = 10*binNo + listOfBits[k]
		return binNo
	def palindromeTest(self, x):
		numToStr = str(x)
		numOfDigits = len(numToStr)
		halfString = numOfDigits//2
		flag = True
		for k in range(halfString):
			flag = flag and numToStr[k] == numToStr[numOfDigits-1-k]
		return flag
	def test_decimalToBinaryCase1(self):
		self.assertTrue(self.decimalToBinary(123) == 1111011)
	def test_decimalToBinaryCase2(self):
		self.assertTrue(self.decimalToBinary(13) == 1101)
	def test_decimalToBinaryCase3(self):
		self.assertTrue(self.decimalToBinary(145) == 10010001)
	def test_palindromeTest1(self):
		self.assertTrue(self.palindromeTest(1234321))
	def test_palindromeTest2(self):
		self.assertTrue(self.palindromeTest(1))
	def test_palindromeTest3(self):
		self.assertTrue(self.palindromeTest(0))
	def test_palindromeTest4(self):
		self.assertTrue(self.palindromeTest(576675))
	def test_palindromeTest5(self):
		self.assertFalse(self.palindromeTest(12334321))
	def test_palindromeTest6(self):
		self.assertFalse(self.palindromeTest(156))
	def test_palindromeTest7(self):
		self.assertFalse(self.palindromeTest(304))
	def test_palindromeTest8(self):
		self.assertFalse(self.palindromeTest(57609675))
	def test_mainDriver(self):
		maxSpan = 1000000
		intendedSum = 0
		for k in range(maxSpan):
			binRepK = self.decimalToBinary(k)
			if self.palindromeTest(k) and self.palindromeTest(binRepK):
				print(
					"The number", k,
					"and its binary equivalent", binRepK,
					"are both equivalent"
					)
				intendedSum += k
		print("The sum of all palindromes =", intendedSum)
		self.assertTrue(True)

if __name__ == "__main__":
	unittest.main()