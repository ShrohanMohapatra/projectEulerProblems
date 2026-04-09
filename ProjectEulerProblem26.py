# ProjectEulerProblem26.py

import unittest
import math

class test_ProjectEulerProblem26(unittest.TestCase):
    def gcdFinder(self, a, b):
        if a > b: return self.gcdFinder(b, a)
        elif b % a == 0: return a
        else: return self.gcdFinder(b%a, a)
    def boolPowerOfOnlyTwoOrFive(self, n):
        bufferForN = n
        while bufferForN % 2 == 0:
            bufferForN = bufferForN // 2
        while bufferForN % 5 == 0:
            bufferForN = bufferForN // 5
        return bufferForN == 1
    def recurringDecimalPatternRecognizer(self, n, maxExpDigits):
        if self.boolPowerOfOnlyTwoOrFive(n): return 0
        else:
            setOfPowersOf10 = [0 for k in range(maxExpDigits+1)]
        powerOf10 = 1
        for k in range(maxExpDigits+1):
            setOfPowersOf10[k] = powerOf10
            powerOf10 = powerOf10 * 10
        startIndex = 0
        endIndex = 0
        for k in range(1, maxExpDigits+1):
            searchFlag = False
            TenPowerK = setOfPowersOf10[k]
            for m in range(k):
                TenPowerM = setOfPowersOf10[m]
                if (TenPowerK - TenPowerM) % n == 0:
                    startIndex = m
                    endIndex = k
                    searchFlag = True
                    break
            if searchFlag: break
        return abs(endIndex - startIndex)
    #### #### #### #### #### #### #### #### #### #### ####
    def test_gcdExample1(self):
        self.assertTrue(self.gcdFinder(7, 10) == 1)
    def test_gcdExample2(self):
        self.assertTrue(self.gcdFinder(10, 14) == 2)
    def test_gcdExample3(self):
        self.assertTrue(self.gcdFinder(3, 15) == 3)
    def test_gcdExample4(self):
        self.assertTrue(self.gcdFinder(12, 15) == 3)
    def test_gcdExample5(self):
        self.assertTrue(self.gcdFinder(17, 119) == 17)
    #### #### #### #### #### #### #### #### #### #### ####
    def test_numberDivisibleByOnly2Or5Example1(self):
        self.assertTrue(self.boolPowerOfOnlyTwoOrFive(100))
    def test_numberDivisibleByOnly2Or5Example2(self):
        self.assertTrue(self.boolPowerOfOnlyTwoOrFive(1000))
    def test_numberDivisibleByOnly2Or5Example3(self):
        self.assertTrue(self.boolPowerOfOnlyTwoOrFive(50))
    def test_numberDivisibleByOnly2Or5Example4(self):
        self.assertTrue(self.boolPowerOfOnlyTwoOrFive(25))
    def test_numberDivisibleByOnly2Or5Example5(self):
        self.assertTrue(self.boolPowerOfOnlyTwoOrFive(2))
    def test_numberDivisibleByOnly2Or5Example6(self):
        self.assertTrue(self.boolPowerOfOnlyTwoOrFive(5))
    def test_numberDivisibleByOnly2Or5Example7(self):
        self.assertTrue(self.boolPowerOfOnlyTwoOrFive(40))
    #### #### #### #### #### #### #### #### #### #### ####
    def test_numberDivisibleByOnly2Or5Example8(self):
        self.assertFalse(self.boolPowerOfOnlyTwoOrFive(3))
    def test_numberDivisibleByOnly2Or5Example9(self):
        self.assertFalse(self.boolPowerOfOnlyTwoOrFive(21))
    def test_numberDivisibleByOnly2Or5Example10(self):
        self.assertFalse(self.boolPowerOfOnlyTwoOrFive(15))
    def test_numberDivisibleByOnly2Or5Example11(self):
        self.assertFalse(self.boolPowerOfOnlyTwoOrFive(17))
    def test_numberDivisibleByOnly2Or5Example12(self):
        self.assertFalse(self.boolPowerOfOnlyTwoOrFive(75))
    def test_numberDivisibleByOnly2Or5Example13(self):
        self.assertFalse(self.boolPowerOfOnlyTwoOrFive(7))
    def test_numberDivisibleByOnly2Or5Example14(self):
        self.assertFalse(self.boolPowerOfOnlyTwoOrFive(42))
    #### #### #### #### #### #### #### #### #### #### ####
    def test_baseCaseExample1(self):
        x = 75
        numberOfDecimalPoints = 20
        listOfDecimalDigits = [
            0, 1, 3, 3, 3,
            3, 3, 3, 3, 3,
            3, 3, 3, 3, 3,
            3, 3, 3, 3, 3
            ]
        powerOf10 = 10
        for k in range(1, numberOfDecimalPoints+1):
            extractedDigit = (powerOf10 // x) % 10
            powerOf10 = powerOf10 * 10
            self.assertEqual(
                listOfDecimalDigits[k-1], extractedDigit
                )
        maxPowersOf10 = 15
        setOfPowersOf10 = [0 for k in range(maxPowersOf10+1)]
        powerOf10 = 1
        for k in range(maxPowersOf10+1):
            setOfPowersOf10[k] = powerOf10
            powerOf10 = powerOf10 * 10
        startIndex = 0
        endIndex = 0
        for k in range(1, maxPowersOf10+1):
            searchFlag = False
            TenPowerK = setOfPowersOf10[k]
            for m in range(k):
                TenPowerM = setOfPowersOf10[m]
                if (TenPowerK - TenPowerM) % x == 0:
                    startIndex = m
                    endIndex = k
                    searchFlag = True
                    break
            if searchFlag: break
        self.assertEqual(abs(endIndex - startIndex), 1)
    def test_baseCaseExample2(self):
        x = 89
        maxPowersOf10 = 160
        setOfPowersOf10 = [0 for k in range(maxPowersOf10+1)]
        powerOf10 = 1
        for k in range(maxPowersOf10+1):
            setOfPowersOf10[k] = powerOf10
            powerOf10 = powerOf10 * 10
        startIndex = 0
        endIndex = 0
        for k in range(1, maxPowersOf10+1):
            searchFlag = False
            TenPowerK = setOfPowersOf10[k]
            for m in range(k):
                TenPowerM = setOfPowersOf10[m]
                if (TenPowerK - TenPowerM) % x == 0:
                    startIndex = m
                    endIndex = k
                    searchFlag = True
                    break
            if searchFlag: break
        self.assertEqual(abs(endIndex - startIndex), 44)
    #### #### #### #### #### #### #### #### #### #### ####
    def test_lengthRecurringDecimalPatternExample1(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(2, 10), 0
            )
    def test_lengthRecurringDecimalPatternExample2(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(3, 10), 1
            )
    def test_lengthRecurringDecimalPatternExample3(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(4, 10), 0
            )
    def test_lengthRecurringDecimalPatternExample4(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(5, 10), 0
            )
    def test_lengthRecurringDecimalPatternExample5(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(6, 10), 1
            )
    def test_lengthRecurringDecimalPatternExample6(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(7, 10), 6
            )
    def test_lengthRecurringDecimalPatternExample7(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(8, 10), 0
            )
    def test_lengthRecurringDecimalPatternExample8(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(9, 10), 1
            )
    def test_lengthRecurringDecimalPatternExample9(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(75, 10), 1
            )
    def test_lengthRecurringDecimalPatternExample10(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(89, 100), 44
            )
    def test_lengthRecurringDecimalPatternExample11(self):
        self.assertEqual(
            self.recurringDecimalPatternRecognizer(83, 100), 41
            )
    #### #### #### #### #### #### #### #### #### #### ####
    def test_mainDriverFunction(self):
        maxNumberDigits = 1000
        maxRepeatList = -1000
        targetD = 1
        print()
        for d in range(2, 1000):
            lengthRepeatList = self.recurringDecimalPatternRecognizer(d, maxNumberDigits)
            if maxRepeatList < lengthRepeatList:
                targetD = d
                maxRepeatList = lengthRepeatList
        self.assertEqual(targetD, 983)
        self.assertEqual(maxRepeatList, 982)
if __name__ == "__main__":
    unittest.main()
