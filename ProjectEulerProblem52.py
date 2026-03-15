# ProjectEulerProblem52.py
# For the time being, this will be one of the problems of last interest.

import unittest

class test_ProjectEulerProblem52(unittest.TestCase):
	def listOfDigits(self, num):
		strNum = list(str(num))
		noOfDigits = len(strNum)
		return [int(strNum[k]) for k in range(noOfDigits)]
	def mainDriverFunction(self):
		maxNum = 150000
		for x in range(3, maxNum):
			listBitsX = self.listOfDigits(x)
			listBitsTwoX = self.listOfDigits(2*x)
			listBitsThreeX = self.listOfDigits(3*x)
			listBitsFourX = self.listOfDigits(4*x)
			listBitsFiveX = self.listOfDigits(5*x)
			listBitsSixX = self.listOfDigits(6*x)
			flagVerifLenTwoX = len(listBitsX) == len(listBitsTwoX)
			flagVerifDigitMatchTwoX = True
			for selectedDigit in listBitsX:
				flagVerifDigitMatchTwoX = flagVerifDigitMatchTwoX and (selectedDigit in listBitsTwoX)
			flagVerifLenThreeX = len(listBitsX) == len(listBitsThreeX)
			flagVerifDigitMatchThreeX = True
			for selectedDigit in listBitsX:
				flagVerifDigitMatchThreeX = flagVerifDigitMatchThreeX and (selectedDigit in listBitsThreeX)
			flagVerifLenFourX = len(listBitsX) == len(listBitsFourX)
			flagVerifDigitMatchFourX = True
			for selectedDigit in listBitsX:
				flagVerifDigitMatchFourX = flagVerifDigitMatchFourX and (selectedDigit in listBitsFourX)
			flagVerifLenFiveX = len(listBitsX) == len(listBitsFiveX)
			flagVerifDigitMatchFiveX = True
			for selectedDigit in listBitsX:
				flagVerifDigitMatchFiveX = flagVerifDigitMatchFiveX and (selectedDigit in listBitsFiveX)
			flagVerifLenSixX = len(listBitsX) == len(listBitsSixX)
			flagVerifDigitMatchSixX = True
			for selectedDigit in listBitsX:
				flagVerifDigitMatchSixX = flagVerifDigitMatchSixX and (selectedDigit in listBitsSixX)
			overallFlag = (
				flagVerifLenTwoX and flagVerifDigitMatchTwoX and \
					flagVerifLenThreeX and flagVerifDigitMatchThreeX and \
					flagVerifDigitMatchFourX and flagVerifDigitMatchFourX and \
					flagVerifLenFiveX and flagVerifDigitMatchFiveX and \
					flagVerifLenSixX and flagVerifDigitMatchSixX
					)
			if overallFlag:
				print("Verified the property for x =", x, " and worked out!")
				break
			else:
				print("Verified the property for x =", x, " but did not work out!")
		return x
	def test_workDigitsV1(self):
		self.assertTrue(self.listOfDigits(123) == [1, 2, 3])
	def test_workDigitsV2(self):
		self.assertTrue(self.listOfDigits(1234) == [1, 2, 3, 4])
	def test_workDigitsV3(self):
		self.assertTrue(self.listOfDigits(12345) == [1, 2, 3, 4, 5])
	def test_defaultTestTrue(self):
		self.assertTrue(True)
	def test_defaultTestFalse(self):
		self.assertFalse(False)
	def test_mainDriver(self):
		circularNumber = self.mainDriverFunction()
		self.assertTrue(circularNumber == 142857)

if __name__ == "__main__":
	unittest.main()