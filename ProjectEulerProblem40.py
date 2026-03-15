# ProjectEulerProblem40.py

import unittest
import math
import random

class test_ProjectEulerProblem40(unittest.TestCase):
	def numOfDigits(self, x):
		return math.ceil(math.log10(x))
	def listOfDigits(self, x):
		strNum = str(x)
		lenStr = len(strNum)
		return [int(strNum[k]) for k in range(lenStr)]
	def truncatedChampernowneConstant(self, numDigits):
		listOfBits = [0.0000 for k in range(numDigits)]
		k = 0
		m = 1
		n = 1
		mMax = self.numOfDigits(numDigits)
		while k < numDigits and m <= mMax:
			if 10**(m-1) <= n and n < 10**m:
				subSetDigits = self.listOfDigits(n)
				n += 1
				flagInternal = False
				for p in range(m):
					if k < numDigits:
						listOfBits[k] = subSetDigits[p]
						k += 1
					else:
						flagInternal = True
						break
				if flagInternal:
					break
			else:
				m += 1
				continue
		return listOfBits
	def driverFunctionGeometricSeriesTest(self, m):
		p = 10
		s = 0
		for k in range(1, m+1):
			s = s + p
			p = p * 10
		t = (10**(m+1)-10)//9
		return abs(s-t)
	def driverFunctionMdigitGroupsTest(self, m):
		p = 1
		s = 0
		for k in range(1, m+1):
			s = s + 9*k*p
			p = p*10
		t = (m+1)*10**m - 1 - (10**(m+1)-10)//9
		return abs(s-t)
	def test_TestCase1NumberOfDigits(self):
		self.assertTrue(self.numOfDigits(123) == 3)
	def test_TestCase2NumberOfDigits(self):
		x = 101 + 898*random.random()
		self.assertTrue(self.numOfDigits(math.ceil(x)) == 3)
	def test_TestCase3NumberOfDigits(self):
		x = 1001 + 8998*random.random()
		self.assertTrue(self.numOfDigits(math.ceil(x)) == 4)
	def test_TestCase4NumberOfDigits(self):
		x = 10001 + 89998*random.random()
		self.assertTrue(self.numOfDigits(math.ceil(x)) == 5)
	def test_TestCase5NumberOfDigits(self):
		x = 100001 + 899998*random.random()
		self.assertTrue(self.numOfDigits(math.ceil(x)) == 6)
	def test_TestCase1ListOfDigits(self):
		x = 432
		expectedListDigits = [4, 3, 2]
		self.assertTrue(self.listOfDigits(x) == expectedListDigits)
	def test_TestCase2ListOfDigits(self):
		x = 432
		expectedListDigits = [4, 3, 2]
		self.assertTrue(self.listOfDigits(x) == expectedListDigits)
	def test_TestCase3ListOfDigits(self):
		x = 13553456789123
		expectedListDigits = [
			1, 3, 5, 5, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3
			]
		self.assertTrue(self.listOfDigits(x) == expectedListDigits)
	def test_truncConstCase1(self):
		expectedListOfBits = [
			1, 2, 3, 4, 5, 6, 7
			]
		self.assertTrue(
			self.truncatedChampernowneConstant(7) == \
				expectedListOfBits
			)
	def test_truncConstCase2(self):
		expectedListOfBits = [
			1, 2, 3, 4, 5, 6, 7, 8
			]
		self.assertTrue(
			self.truncatedChampernowneConstant(8) == \
				expectedListOfBits
			)
	def test_truncConstCase3(self):
		expectedListOfBits = [
			1, 2, 3, 4, 5, 6, 7, 8, 9
			]
		self.assertTrue(
			self.truncatedChampernowneConstant(9) == \
				expectedListOfBits
			)
	def test_truncConstCase4(self):
		expectedListOfBits = [
			1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2
			]
		self.assertTrue(
			self.truncatedChampernowneConstant(15) == \
				expectedListOfBits
			)
	def test_truncConstCase5(self):
		expectedListOfBits = [
			1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0,
			1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9
			]
		self.assertTrue(
			self.truncatedChampernowneConstant(29) == \
				expectedListOfBits
			)
	def test_truncConstCase6(self):
		expectedListOfBits = [
			1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1,
			1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 2, 0
			]
		self.assertTrue(
			self.truncatedChampernowneConstant(31) == \
				expectedListOfBits
			)
	def test_truncConstCase7(self):
		expectedListOfBits = [
			1, 2, 3, 4, 5, 6, 7, 8, 9,
			1,0, 1,1, 1,2, 1,3, 1,4, 1,5, 1,6, 1,7, 1,8, 1,9,
			2,0, 2,1, 2,2, 2,3, 2,4, 2,5, 2,6, 2,7, 2,8, 2,9,
			3,0, 3,1, 3,2, 3,3, 3,4, 3,5, 3,6, 3,7, 3,8, 3,9,
			4,0, 4,1, 4,2, 4,3, 4,4, 4,5, 4,6, 4,7, 4,8, 4,9,
			5,0, 5,1, 5,2, 5,3, 5,4, 5,5, 5,6, 5,7, 5,8, 5,9,
			6,0, 6,1, 6,2, 6,3, 6,4, 6,5, 6,6, 6,7, 6,8, 6,9,
			7,0, 7,1, 7,2, 7,3, 7,4, 7,5, 7,6, 7,7, 7,8, 7,9,
			8,0, 8,1, 8,2, 8,3, 8,4, 8,5, 8,6, 8,7, 8,8, 8,9,
			9,0, 9,1, 9,2, 9,3, 9,4, 9,5, 9,6, 9,7, 9,8, 9,9
			]
		self.assertTrue(
			self.truncatedChampernowneConstant(189) == \
				expectedListOfBits
			)
	def test_truncConstCase8(self):
		expectedListOfBits = [
			1, 2, 3, 4, 5, 6, 7, 8, 9,
			1,0, 1,1, 1,2, 1,3, 1,4, 1,5, 1,6, 1,7, 1,8, 1,9,
			2,0, 2,1, 2,2, 2,3, 2,4, 2,5, 2,6, 2,7, 2,8, 2,9,
			3,0, 3,1, 3,2, 3,3, 3,4, 3,5, 3,6, 3,7, 3,8, 3,9,
			4,0, 4,1, 4,2, 4,3, 4,4, 4,5, 4,6, 4,7, 4,8, 4,9,
			5,0, 5,1, 5,2, 5,3, 5,4, 5,5, 5,6, 5,7, 5,8, 5,9,
			6,0, 6,1, 6,2, 6,3, 6,4, 6,5, 6,6, 6,7, 6,8, 6,9,
			7,0, 7,1, 7,2, 7,3, 7,4, 7,5, 7,6, 7,7, 7,8, 7,9,
			8,0, 8,1, 8,2, 8,3, 8,4, 8,5, 8,6, 8,7, 8,8, 8,9,
			9,0, 9,1, 9,2, 9,3, 9,4, 9,5, 9,6, 9,7, 9,8, 9,9,
			1,0,0, 1,0,1, 1,0,2, 1,0,3, 1,0,4, 1,0,5, 1,0,6, 1,0,7, 1,0,8, 1,0,9,
			1,1,0, 1,1,1, 1,1,2, 1,1,3, 1,1,4, 1,1,5, 1,1,6, 1,1,7, 1,1,8, 1,1,9,
			1,2,0, 1,2,1, 1,2,2, 1,2,3, 1,2,4, 1,2,5, 1,2,6, 1,2,7, 1,2,8, 1,2,9
			]
		self.assertTrue(
			self.truncatedChampernowneConstant(279) == \
				expectedListOfBits
			)
	def test_geomSeriesVerifV1(self):
		self.assertTrue(self.driverFunctionGeometricSeriesTest(1) == 0)
	def test_geomSeriesVerifV2(self):
		self.assertTrue(self.driverFunctionGeometricSeriesTest(2) == 0)
	def test_geomSeriesVerifV3(self):
		self.assertTrue(self.driverFunctionGeometricSeriesTest(3) == 0)
	def test_geomSeriesVerifV4(self):
		self.assertTrue(self.driverFunctionGeometricSeriesTest(4) == 0)
	def test_geomSeriesVerifV5(self):
		self.assertTrue(self.driverFunctionGeometricSeriesTest(5) == 0)
	def test_geomSeriesVerifV6(self):
		self.assertTrue(self.driverFunctionGeometricSeriesTest(6) == 0)
	def test_geomSeriesVerifV7(self):
		self.assertTrue(self.driverFunctionGeometricSeriesTest(7) == 0)
	def test_mDigitGroupsV1(self):
		self.assertTrue(self.driverFunctionMdigitGroupsTest(1) == 0)
	def test_mDigitGroupsV2(self):
		self.assertTrue(self.driverFunctionMdigitGroupsTest(2) == 0)
	def test_mDigitGroupsV3(self):
		self.assertTrue(self.driverFunctionMdigitGroupsTest(3) == 0)
	def test_mDigitGroupsV4(self):
		self.assertTrue(self.driverFunctionMdigitGroupsTest(4) == 0)
	def test_mDigitGroupsV5(self):
		self.assertTrue(self.driverFunctionMdigitGroupsTest(5) == 0)
	def test_mDigitGroupsV6(self):
		self.assertTrue(self.driverFunctionMdigitGroupsTest(6) == 0)
	def test_mDigitGroupsV7(self):
		self.assertTrue(self.driverFunctionMdigitGroupsTest(7) == 0)
	def test_doubleDigitExtractors(self):
		listOfDoubleDigitTruncs = self.truncatedChampernowneConstant(189)
		for n in range(10, 190):
			s = (9 + math.ceil((n-9)/2))
			if n%2:
				self.assertTrue(listOfDoubleDigitTruncs[n-1] == s%10)
			else:
				self.assertTrue(listOfDoubleDigitTruncs[n-1] == s//10)
	def test_TotalFiveDigitGroups(self):
		m = 5
		TmExpected = (m+1)*10**m - m - 1 - (10**(m+1)-10)//9
		TmObserved = 0
		for x in range(1, 10**m):
			TmObserved = TmObserved + self.numOfDigits(x)
		self.assertTrue(abs(TmExpected-TmObserved) == 0)
	def test_TotalEightDigitGroups(self):
		m = 8
		TmExpected = (m+1)*10**m - m - 1 - (10**(m+1)-10)//9
		TmObserved = 0
		for x in range(1, 10**m):
			TmObserved = TmObserved + self.numOfDigits(x)
		self.assertTrue(abs(TmExpected-TmObserved) == 0)
	def test_JustFiveDigitGroups(self):
		m = 5
		TmMinusOne = m*10**(m-1) - 1 - (10**m-10)//9
		Tm = (m+1)*10**m - 1 - (10**(m+1)-10)//9
		expDigits = 9*m*10**(m-1)
		self.assertTrue(abs(abs(Tm-TmMinusOne) - expDigits) < 1.e-16)
	def test_JustEightDigitGroups(self):
		m = 8
		TmMinusOne = m*10**(m-1) - 1 - (10**m-10)//9
		Tm = (m+1)*10**m - 1 - (10**(m+1)-10)//9
		expDigits = 9*m*10**(m-1)
		self.assertTrue(abs(abs(Tm-TmMinusOne) - expDigits) < 1.e-16)
	def test_JustFourteenDigitGroups(self):
		m = 14
		TmMinusOne = m*10**(m-1) - 1 - (10**m-10)//9
		Tm = (m+1)*10**m - 1 - (10**(m+1)-10)//9
		expDigits = 9*m*10**(m-1)
		self.assertTrue(abs(abs(Tm-TmMinusOne) - expDigits) < 1.e-16)
	def test_ActualFiveDigitGroups(self):
		self.assertTrue(True)
if __name__ == "__main__":
	unittest.main()