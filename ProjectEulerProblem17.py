# ProjectEulerProblem17.py

import unittest
import math

class test_ProjectEulerProblem17(unittest.TestCase):
	singleDigitDict = {
		0: "", 1: "one", 2: "two", 3: "three",
		4: "four", 5: "five", 6: "six",
		7: "seven", 8: "eight", 9: "nine"
		}
	specialDoubleDigitDict = {
		10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
		14: "fourteen", 15: "fifteen", 16: "sixteen",
		17: "seventeen", 18: "eighteen", 19: "nineteen"
		}
	generalDoubleDigitDict = {
		2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
		6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
		}
	def numberNameGenerator(self, n):
		if n == 1:
			return self.singleDigitDict[1]
		elif n == 10:
			numberOfDigits = 2
		elif n == 100:
			numberOfDigits = 3
		else:
			numberOfDigits = math.ceil(math.log10(n))
		listOfDigits = [0 for k in range(numberOfDigits)]
		z = n
		for k in range(numberOfDigits):
			listOfDigits[numberOfDigits-1-k] = z%10
			z = z//10
		if numberOfDigits == 1:
			return self.singleDigitDict[n]
		elif numberOfDigits == 2:
			if listOfDigits[0] == 1:
				strNumberName = self.specialDoubleDigitDict[n]
			else:
				strNumberName = self.generalDoubleDigitDict[listOfDigits[0]] \
									+ ("-" + self.singleDigitDict[listOfDigits[1]]
										if listOfDigits[1] else ""
										)
			return strNumberName
		else:
			if n%100 == 0:
				return self.singleDigitDict[listOfDigits[0]] + " hundred"
			else:
				return self.singleDigitDict[listOfDigits[0]] \
						+ " hundred and " + self.numberNameGenerator(n%100)
	def totalNumberNameLetterCount(self):
		totalLetterCount = 0
		for number in range(1, 1000):
			numberName = self.numberNameGenerator(number)
			charCountNumberName = len(numberName)
			numberNameLetters = 0
			for m in range(charCountNumberName):
				unicodeNumber = ord(numberName[m])
				if 97 <= unicodeNumber and unicodeNumber <= 122:
					numberNameLetters = numberNameLetters + 1
			totalLetterCount = totalLetterCount + numberNameLetters
		numberName = "one thousand"
		charCountNumberName = len(numberName)
		numberNameLetters = 0
		for m in range(charCountNumberName):
			unicodeNumber = ord(numberName[m])
			if 97 <= unicodeNumber and unicodeNumber <= 122:
				numberNameLetters = numberNameLetters + 1
		totalLetterCount = totalLetterCount + numberNameLetters
		return totalLetterCount
	def test_numberNameGenCase1(self):
		self.assertTrue(
			self.numberNameGenerator(2) == "two"
			)
	def test_numberNameGenCase2(self):
		self.assertTrue(
			self.numberNameGenerator(3) == "three"
			)
	def test_numberNameGenCase3(self):
		self.assertTrue(
			self.numberNameGenerator(6) == "six"
			)
	def test_numberNameGenCase4(self):
		self.assertTrue(
			self.numberNameGenerator(16) == "sixteen"
			)
	def test_numberNameGenCase5(self):
		self.assertTrue(
			self.numberNameGenerator(27) == "twenty-seven"
			)
	def test_numberNameGenCase6(self):
		self.assertTrue(
			self.numberNameGenerator(43) == "forty-three"
			)
	def test_numberNameGenCase7(self):
		self.assertTrue(
			self.numberNameGenerator(50) == "fifty"
			)
	def test_numberNameGenCase8(self):
		self.assertTrue(
			self.numberNameGenerator(72) == "seventy-two"
			)
	def test_numberNameGenCase9(self):
		self.assertTrue(
			self.numberNameGenerator(86) == "eighty-six"
			)
	def test_numberNameGenCase10(self):
		self.assertTrue(
			self.numberNameGenerator(100) == "one hundred"
			)
	def test_numberNameGenCase11(self):
		self.assertTrue(
			self.numberNameGenerator(101) == "one hundred and one"
			)
	def test_numberNameGenCase12(self):
		self.assertTrue(
			self.numberNameGenerator(200) == "two hundred"
			)
	def test_numberNameGenCase13(self):
		self.assertTrue(
			self.numberNameGenerator(256) == "two hundred and fifty-six"
			)
	def test_numberNameGenCase14(self):
		self.assertTrue(
			self.numberNameGenerator(611) == "six hundred and eleven"
			)
	def test_numberNameGenCase15(self):
		self.assertTrue(
			self.numberNameGenerator(850) == "eight hundred and fifty"
			)
	def test_numberNameGenCase16(self):
		self.assertTrue(
			self.numberNameGenerator(407) == "four hundred and seven"
			)
	def test_numberNameCount(self):
		print(self.totalNumberNameLetterCount())
		self.assertTrue(True)

if __name__ == "__main__":
	unittest.main()
