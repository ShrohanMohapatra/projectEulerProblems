# ProjectEulerProblem56.py

import unittest

class test_ProjectEulerProblem56(unittest.TestCase):
	def maximumDigitSumDriver(self):
		maxDigitSum = -1000
		for a in range(2, 100):
			for b in range(2, 100):
				strDigs = str(a**b)
				numOfDigs = len(strDigs)
				listOfDigs = [int(strDigs[k]) for k in range(numOfDigs)]
				sumOfDigs = sum(listOfDigs)
				if maxDigitSum < sumOfDigs:
					maxDigitSum = sumOfDigs
		return maxDigitSum
	def test_DefaultCase1(self):
		self.assertTrue(True)
	def test_DefaultCase2(self):
		self.assertFalse(False)
	def test_maximumDigitSumDriver(self):
		print(self.maximumDigitSumDriver())
		self.assertTrue(True)

if __name__ == "__main__":
	unittest.main()