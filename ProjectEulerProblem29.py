# ProjectEulerProblem29.py

import unittest
import math

class test_ProjectEulerProblem29(unittest.TestCase):
	def distinctPowersSequenceDriver(self, nMax):
		seqDistTerms = []
		for k in range(nMax-1):
			for m in range(nMax-1):
				powTerm = (k+2)**(m+2)
				if powTerm not in seqDistTerms:
					seqDistTerms.append(powTerm)
		return len(seqDistTerms)
	def test_defaultTest1(self):
		self.assertTrue(True)
	def test_defaultTest2(self):
		self.assertFalse(False)
	def test_maxSpan5Case(self):
		self.assertTrue(
			self.distinctPowersSequenceDriver(5) == 15
			)
	def test_maxSpan7Case(self):
		self.assertTrue(
			self.distinctPowersSequenceDriver(7) == 34
			)
	def test_maxSpan100Case(self):
		self.assertTrue(
			self.distinctPowersSequenceDriver(100) == 9183
			)

if __name__ == "__main__":
	unittest.main()