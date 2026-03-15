# ProjectEulerProblemFour.py

import unittest

class test_ProjectEulerProblemFour(unittest.TestCase):
	def palindromeNumber(self, num):
		strDigits = str(num)
		numOfDigits = len(strDigits)
		numOfDigitsBy2 = numOfDigits//2
		flag = True
		for k in range(numOfDigitsBy2):
			if strDigits[k] != strDigits[numOfDigits-1-k]:
				flag = False
				break
		return flag
	def palindromeSieveSearch(self):
		palindromeList = []
		for k1 in range(900, 1000):
			for k2 in range(900, 1000):
				k3 = k1*k2
				if self.palindromeNumber(k3):
					palindromeList.append(k3)
		return max(palindromeList)
	def test_DefaultTest1(self):
		self.assertTrue(True)
	def test_DefaultTest2(self):
		self.assertFalse(False)
	def test_palindromeTestCase1(self):
		self.assertTrue(self.palindromeNumber(123321))
	def test_palindromeTestCase2(self):
		self.assertTrue(self.palindromeNumber(12321))
	def test_palindromeTestCase3(self):
		self.assertTrue(self.palindromeNumber(5445))
	def test_palindromeTestCase4(self):
		self.assertTrue(self.palindromeNumber(121))
	def test_palindromeTestCase5(self):
		self.assertTrue(self.palindromeNumber(787))
	def test_palindromeTestCase6(self):
		self.assertTrue(self.palindromeNumber(555))
	def test_palindromeTestCase7(self):
		self.assertTrue(self.palindromeNumber(55))
	def test_palindromeTestCase8(self):
		self.assertTrue(self.palindromeNumber(5))
	def test_palindromeTestCase9(self):
		self.assertFalse(self.palindromeNumber(12345))
	def test_palindromeTestCase10(self):
		self.assertFalse(self.palindromeNumber(543221))
	def test_palindromeTestCase11(self):
		self.assertFalse(self.palindromeNumber(5437445))
	def test_palindromeTestCase12(self):
		self.assertFalse(self.palindromeNumber(999*999))
	def test_RealTest(self):
		self.assertTrue(self.palindromeSieveSearch() == 906609)

if __name__ == "__main__":
	unittest.main()