# ProjectEulerProblem92.py

import unittest
import math

class test_ProjectEulerProblem92(unittest.TestCase):
    numberChainInfCycle = [89, 145, 42, 20, 4, 16, 37, 58]
    def numberOfDigits(self, x):
        powerOfTen = 0
        z = x
        while z > 0:
            if z % 10 != 0 and z != 1:
                return math.ceil(math.log10(x))
            else:
                z = z // 10
                powerOfTen = powerOfTen + 1
        return powerOfTen
    def listOfDigits(self, x):
        digitCount = self.numberOfDigits(x)
        digitList = [0 for k in range(digitCount)]
        z = x
        for k in range(digitCount-1,-1,-1):
            digitList[k] = z % 10
            z = z // 10
        return digitList
    def sumSqDigits(self, x):
        digitCount = self.numberOfDigits(x)
        digitList = self.listOfDigits(x)
        sumOfSquareOfDigits = 0
        for k in range(digitCount):
            sumOfSquareOfDigits = sumOfSquareOfDigits + digitList[k]**2
        return sumOfSquareOfDigits
    def numberChainList(self, x):
        returnList = [x]
        z = x
        while True:
            sumSqDigitZ = self.sumSqDigits(z)
            if sumSqDigitZ not in returnList:
                returnList.append(sumSqDigitZ)
                z = sumSqDigitZ
            else:
                returnList.append(sumSqDigitZ)
                break
        return returnList
    def mainProblemStatementHandle(self):
        scenario1 = "Considering sharp arrival at 89"
        scenario2 = "Considering whole infinite cycle with 89"
        arrivalCount = {scenario1: 0, scenario2: 0}
        for k in range(1, 10**7):
            numberChain = self.numberChainList(k)
            lastElem = numberChain[-1]
            if lastElem == 89:
                arrivalCount[scenario1] = arrivalCount[scenario1] + 1
            if lastElem in self.numberChainInfCycle:
                arrivalCount[scenario2] = arrivalCount[scenario2] + 1
        return arrivalCount
    def test_digitCountTestCase1(self):
        self.assertTrue(self.numberOfDigits(1) == 1)
    def test_digitCountTestCase2(self):
        self.assertTrue(self.numberOfDigits(10) == 2)
    def test_digitCountTestCase3(self):
        self.assertTrue(self.numberOfDigits(100) == 3)
    def test_digitCountTestCase4(self):
        self.assertTrue(self.numberOfDigits(1000) == 4)
    def test_digitCountTestCase5(self):
        self.assertTrue(self.numberOfDigits(10000) == 5)
    def test_digitCountTestCase6(self):
        self.assertTrue(self.numberOfDigits(5268) == 4)
    def test_digitCountTestCase7(self):
        self.assertTrue(self.numberOfDigits(8327775461) == 10)
    def test_digitCountTestCase8(self):
        self.assertTrue(self.numberOfDigits(2000) == 4)
    def test_digitCountTestCase9(self):
        self.assertTrue(self.numberOfDigits(20001) == 5)
    def test_digitCountTestCase10(self):
        self.assertTrue(self.numberOfDigits(5520) == 4)
    def test_digitListTestCase1(self):
        self.assertTrue(self.listOfDigits(5368) == [5, 3, 6, 8])
    def test_digitListTestCase2(self):
        self.assertTrue(self.listOfDigits(2000) == [2, 0, 0, 0])
    def test_digitListTestCase3(self):
        self.assertTrue(self.listOfDigits(2001) == [2, 0, 0, 1])
    def test_digitListTestCase4(self):
        self.assertTrue(self.listOfDigits(1) == [1])
    def test_digitListTestCase5(self):
        self.assertTrue(self.listOfDigits(2) == [2])
    def test_digitListTestCase6(self):
        self.assertTrue(self.listOfDigits(3) == [3])
    def test_digitListTestCase7(self):
        self.assertTrue(self.listOfDigits(5) == [5])
    def test_digitListTestCase8(self):
        self.assertTrue(self.listOfDigits(14000) == [1, 4, 0, 0, 0])
    def test_digitListTestCase9(self):
        self.assertTrue(self.listOfDigits(100000) == [1, 0, 0, 0, 0, 0])
    def test_digitListTestCase10(self):
        self.assertTrue(self.listOfDigits(1000) == [1, 0, 0, 0])
    def test_sumSquareDigitsCase1(self):
        self.assertTrue(self.sumSqDigits(15263) == 75)
    def test_sumSquareDigitsCase2(self):
        self.assertTrue(self.sumSqDigits(7549) == 171)
    def test_sumSquareDigitsCase3(self):
        self.assertTrue(self.sumSqDigits(452) == 45)
    def test_sumSquareDigitsCase4(self):
        self.assertTrue(self.sumSqDigits(785) == 138)
    def test_sumSquareDigitsCase5(self):
        self.assertTrue(self.sumSqDigits(12345) == 55)
    def test_sumSquareDigitsCase6(self):
        self.assertTrue(self.sumSqDigits(7) == 49)
    def test_sumSquareDigitsCase7(self):
        self.assertTrue(self.sumSqDigits(12) == 5)
    def test_sumSquareDigitsCase8(self):
        self.assertTrue(self.sumSqDigits(4658) == 141)
    def test_sumSquareDigitsCase9(self):
        self.assertTrue(self.sumSqDigits(14523) == 55)
    def test_sumSquareDigitsCase10(self):
        self.assertTrue(self.sumSqDigits(10**9) == 1)
    def test_numberChainListTestCase1(self):
        numberChain = self.numberChainList(44)
        self.assertTrue(numberChain[-1] == 1)
        self.assertEqual(numberChain, [44, 32, 13, 10, 1, 1])
    def test_numberChainListTestCase2(self):
        numberChain = self.numberChainList(85)
        expectedNumberChain = [
            85, 89, 145, 42, 20, 4, 16, 37, 58, 89
            ]
        self.assertTrue(numberChain[-1] == 89)
        self.assertEqual(numberChain, expectedNumberChain)
    def test_numberChainListTestCase3(self):
        numberChain = self.numberChainList(185)
        lastElement = numberChain[-1]
        # print("lastElement =", lastElement)
        self.assertTrue(lastElement == 37)
        self.assertTrue(
            lastElement == 1 or lastElement in self.numberChainInfCycle
            )
    def test_numberChainListTestCase4(self):
        numberChain = self.numberChainList(289)
        lastElement = numberChain[-1]
        # print("lastElement =", lastElement)
        self.assertTrue(lastElement == 145)
        self.assertTrue(
            lastElement == 1 or lastElement in self.numberChainInfCycle
            )
    def test_numberChainListTestCase5(self):
        numberChain = self.numberChainList(2026)
        lastElement = numberChain[-1]
        self.assertTrue(lastElement == 1)
        self.assertTrue(
            lastElement == 1 or lastElement in self.numberChainInfCycle
            )
    def test_numberChainListTestCase6(self):
        numberChain = self.numberChainList(15251)
        lastElement = numberChain[-1]
        self.assertTrue(lastElement == 37)
        self.assertTrue(
            lastElement == 1 or lastElement in self.numberChainInfCycle
            )
    def test_numberChainListTestCase7(self):
        numberChain = self.numberChainList(452)
        lastElement = numberChain[-1]
        self.assertTrue(lastElement == 89)
        self.assertTrue(
            lastElement == 1 or lastElement in self.numberChainInfCycle
            )
    def test_mainProblemStatementDriver(self):
        arrivalCount = self.mainProblemStatementHandle()
        self.assertEqual(
            arrivalCount["Considering sharp arrival at 89"],
            4006299
            )
        self.assertEqual(
            arrivalCount["Considering whole infinite cycle with 89"],
            8581146
            )

if __name__ == "__main__":
    unittest.main()