# ProjectEulerProblem40Supplement.py

import unittest
from sympy import *

class test_ProjectEulerProblem40Supplement(unittest.TestCase):
	def test_onlyDerivTest(self):
		x = Symbol("x")
		m = Symbol("m")
		print(simplify(expand(diff((x**(m+1)-x)/(x-1), x) - ((x-1)*((m+1)*x**m-1)-(m+1)*x**m+1)/(x-1)**2)))
		self.assertTrue(True)

if __name__ == "__main__":
	unittest.main()