# ProjectEulerProblem47.py

import unittest
import math

class test_ProjectEulerProblem47(unittest.TestCase):
    def primalityTest(self, x):
        if x == 1:
            return False
        elif x == 2:
            return True
        ceilSqrtX = math.ceil(math.sqrt(x))
        for k in range(2, ceilSqrtX+1):
            if x % k == 0:
                return False
        return True
    def primeFactorsDataStructure(self, inputNumber, maxPrimeThreshold):
        bufferPrimeList = []
        dictPrimeFactors = {}
        for k in range(2, maxPrimeThreshold+1):
            if self.primalityTest(k):
                bufferPrimeList.append(k)
        zNumber = inputNumber
        for prime in bufferPrimeList:
            exponentOfPrime = 0
            while zNumber % prime == 0:
                zNumber = zNumber // prime
                exponentOfPrime = exponentOfPrime + 1
            if exponentOfPrime!=0:
                dictPrimeFactors[prime] = exponentOfPrime
        return dictPrimeFactors
    def twoConsecutivePosIntsDistinctPrimes(self, maxScan, maxPrimeThreshold):
        bufferPrimeList = []
        dictPrimeFactorV1 = {}
        dictPrimeFactorV2 = {}
        for k in range(2, maxPrimeThreshold+1):
            if self.primalityTest(k):
                bufferPrimeList.append(k)
        for n in range(2, maxScan):
            zNumber1 = n
            zNumber2 = n+1
            for prime in bufferPrimeList:
                exponentOfPrime1 = 0
                while zNumber1 % prime == 0:
                    zNumber1 = zNumber1 // prime
                    exponentOfPrime1 = exponentOfPrime1 + 1
                if exponentOfPrime1!=0:
                    dictPrimeFactorV1[prime] = exponentOfPrime1
            for prime in bufferPrimeList:
                exponentOfPrime2 = 0
                while zNumber2 % prime == 0:
                    zNumber2 = zNumber2 // prime
                    exponentOfPrime2 = exponentOfPrime2 + 1
                if exponentOfPrime2!=0:
                    dictPrimeFactorV2[prime] = exponentOfPrime2
            if len(dictPrimeFactorV1.keys()) == 2 and len(dictPrimeFactorV2.keys()) == 2:
                break
            dictPrimeFactorV1 = {}
            dictPrimeFactorV2 = {}
        return (n, n+1)
    def threeConsecutivePosIntsDistinctPrimes(self, maxScan, maxPrimeThreshold):
        bufferPrimeList = []
        dictPrimeFactorV1 = {}
        dictPrimeFactorV2 = {}
        dictPrimeFactorV3 = {}
        for k in range(2, maxPrimeThreshold+1):
            if self.primalityTest(k):
                bufferPrimeList.append(k)
        for n in range(2, maxScan+1):
            dictPrimeFactorV1 = {}
            dictPrimeFactorV2 = {}
            dictPrimeFactorV3 = {}
            zNumber1 = n
            zNumber2 = n+1
            zNumber3 = n+2
            for prime in bufferPrimeList:
                exponentOfPrime1 = 0
                while zNumber1 % prime == 0:
                    zNumber1 = zNumber1 // prime
                    exponentOfPrime1 = exponentOfPrime1 + 1
                if exponentOfPrime1!=0:
                    dictPrimeFactorV1[prime] = exponentOfPrime1
            for prime in bufferPrimeList:
                exponentOfPrime2 = 0
                while zNumber2 % prime == 0:
                    zNumber2 = zNumber2 // prime
                    exponentOfPrime2 = exponentOfPrime2 + 1
                if exponentOfPrime2!=0:
                    dictPrimeFactorV2[prime] = exponentOfPrime2
            for prime in bufferPrimeList:
                exponentOfPrime3 = 0
                while zNumber3 % prime == 0:
                    zNumber3 = zNumber3 // prime
                    exponentOfPrime3 = exponentOfPrime3 + 1
                if exponentOfPrime3!=0:
                    dictPrimeFactorV3[prime] = exponentOfPrime3
            checkFlag = len(dictPrimeFactorV1.keys()) == 3 \
                            and len(dictPrimeFactorV2.keys()) == 3 \
                            and len(dictPrimeFactorV3.keys()) == 3
            if checkFlag: break
        return (n, n+1, n+2)
    def fourConsecutivePosIntsDistinctPrimes(self, maxScan, maxPrimeThreshold):
        bufferPrimeList = []
        dictPrimeFactorList = {}
        for n in range(2, maxScan+1):
            dictPrimeFactorList[n] = {}
        for k in range(2, maxPrimeThreshold+1):
            if self.primalityTest(k):
                bufferPrimeList.append(k)
        for n in range(2, maxScan+1):
            zNumber = n
            for prime in bufferPrimeList:
                exponentOfPrime = 0
                while zNumber % prime == 0:
                    zNumber = zNumber // prime
                    exponentOfPrime = exponentOfPrime + 1
                if exponentOfPrime!=0:
                    dictPrimeFactorList[n][prime] = exponentOfPrime
        for n in range(2, maxScan-2):
            primeFactorListNdictKeys = dictPrimeFactorList[n].keys()
            primeFactorListNplusOnedictKeys = dictPrimeFactorList[n+1].keys()
            primeFactorListNplusTwodictKeys = dictPrimeFactorList[n+2].keys()
            primeFactorListNplusThreedictKeys = dictPrimeFactorList[n+3].keys()
            checkFlag = len(primeFactorListNdictKeys) == 4 \
                            and len(primeFactorListNplusOnedictKeys) == 4 \
                            and len(primeFactorListNplusTwodictKeys) == 4 \
                            and len(primeFactorListNplusThreedictKeys) == 4
            if checkFlag:
                return (n, n+1, n+2, n+3)
        return (0, 0, 0, 0)
    def test_primalityCheckCase1(self):
        self.assertTrue(self.primalityTest(3))
    def test_primalityCheckCase2(self):
        self.assertFalse(self.primalityTest(4))
    def test_primalityCheckCase3(self):
        self.assertTrue(self.primalityTest(5))
    def test_primalityCheckCase4(self):
        self.assertTrue(self.primalityTest(7))
    def test_primalityCheckCase5(self):
        self.assertFalse(self.primalityTest(9))
    def test_primalityCheckCase6(self):
        self.assertTrue(self.primalityTest(11))
    def test_primalityCheckCase7(self):
        self.assertTrue(self.primalityTest(13))
    def test_primalityCheckCase8(self):
        self.assertTrue(self.primalityTest(17))
    def test_primalityCheckCase9(self):
        self.assertTrue(self.primalityTest(19))
    def test_primalityCheckCase10(self):
        self.assertFalse(self.primalityTest(21))
    def test_primalityCheckCase11(self):
        self.assertTrue(self.primalityTest(23))
    def test_primeFactorizationCase1(self):
        self.assertTrue(self.primeFactorsDataStructure(15, 25) == {3: 1, 5: 1})
    def test_primeFactorizationCase2(self):
        self.assertTrue(self.primeFactorsDataStructure(14, 25) == {2: 1, 7: 1})
    def test_primeFactorizationCase3(self):
        self.assertTrue(self.primeFactorsDataStructure(8, 12) == {2: 3})
    def test_primeFactorizationCase4(self):
        self.assertTrue(self.primeFactorsDataStructure(7, 12) == {7: 1})
    def test_primeFactorizationCase5(self):
        dictPrimeFactors = self.primeFactorsDataStructure(337500, 1000)
        self.assertTrue(dictPrimeFactors == {2: 2, 3: 3, 5: 5})
        self.assertTrue(len(dictPrimeFactors.keys()) == 3)
    def test_twoConsecutivePosIntsPrimeFactorsCheck(self):
        self.assertEqual(self.twoConsecutivePosIntsDistinctPrimes(20, 20), (14, 15))
    def test_threeConsecutivePosIntsPrimeFactorsCheck(self):
        self.assertEqual(self.threeConsecutivePosIntsDistinctPrimes(1000, 750), (644, 645, 646))
    def test_fourConsecutivePosIntsPrimeFactorsCheck(self):
        self.assertTrue(self.fourConsecutivePosIntsDistinctPrimes(2*10**5, 750) == (134043, 134044, 134045, 134046))


if __name__ == "__main__":
    unittest.main()