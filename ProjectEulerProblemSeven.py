# ProjectEulerProblemSeven.py

import unittest

class test_ProjectEulerProblemSeven(unittest.TestCase):
	def nThPrime(self, n):
		if n == 1:
			return 2
		else:
			listOfPrimes = [0 for k1 in range(n+2)]
			listOfPrimes[1] = 2
			for k2 in range(2, n+1):
				if n == 10001:
					print(
						"listOfPrimes["+str(k2-1)+"] = ", listOfPrimes[k2-1],
						": Last index =", n
						)
				prevPrime = listOfPrimes[k2-1]
				x = prevPrime + 1
				while True:
					flag = True
					for k3 in range(2, prevPrime+1):
						if x % k3 == 0:
							flag = False
							break
					if flag: break
					else: x = x + 1
				listOfPrimes[k2] = x
				if n == 10001:
					print(
						"listOfPrimes["+str(k2)+"] = ", listOfPrimes[k2],
						": Last index =", n
						)
			return listOfPrimes[n]

	def test_DefaultTest1(self):
		self.assertTrue(True)
	def test_DefaultTest2(self):
		self.assertFalse(False)
	def test_NthPrimeTestCase1(self):
		self.assertTrue(self.nThPrime(1) == 2)
	def test_NthPrimeTestCase2(self):
		self.assertTrue(self.nThPrime(2) == 3)
	def test_NthPrimeTestCase3(self):
		self.assertTrue(self.nThPrime(3) == 5)
	def test_NthPrimeTestCase4(self):
		self.assertTrue(self.nThPrime(4) == 7)
	def test_NthPrimeTestCase5(self):
		self.assertTrue(self.nThPrime(5) == 11)
	def test_NthPrimeTestCase6(self):
		self.assertTrue(self.nThPrime(6) == 13)
	def test_NthPrimeTestCase7(self):
		self.assertTrue(self.nThPrime(7) == 17)
	def test_NthPrimeTestCase8(self):
		self.assertTrue(self.nThPrime(10001) == 104743)

if __name__ == "__main__":
	unittest.main()