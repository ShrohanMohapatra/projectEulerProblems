# ProjectEulerProblem808.py

import unittest
import math

class test_ProjectEulerProblem808Version1(unittest.TestCase):
    def primalityTest(self, n):
        if n <= 3: return True
        else:
            ceilSqrtN = math.ceil(math.sqrt(n))
            for k in range(2, ceilSqrtN+1):
                if n % k == 0:
                    return False
            return True
    def numberOfDigits(self, n):
        boolPowerOf10 = True
        countPowerOf10 = 1
        bufferForN = n
        while bufferForN > 1:
            if bufferForN % 10 != 0:
                boolPowerOf10 = False
                break
            else:
                countPowerOf10 = countPowerOf10 + 1
                bufferForN = bufferForN // 10
        if boolPowerOf10:
            return countPowerOf10
        else:
            return math.ceil(math.log10(n))
    def listOfDigits(self, n):
        digitCount = self.numberOfDigits(n)
        returnList = [0 for k in range(digitCount)]
        bufferForN = n
        for k in range(digitCount-1, -1, -1):
            returnList[k] = bufferForN % 10
            bufferForN = bufferForN // 10
        return returnList
    def palindromeDigitsCheck(self, n):
        digitCount = self.numberOfDigits(n)
        digitList = self.listOfDigits(n)
        boolePalindrome = True
        for k in range(digitCount//2):
            boolePalindrome = boolePalindrome and digitList[k] == digitList[digitCount-k-1]
        return boolePalindrome
    def numberFormedFromDigitList(self, digitList):
        digitCount = len(digitList)
        totalNumber = 0
        powerOf10 = 1
        for k in range(digitCount-1, -1, -1):
            totalNumber = totalNumber + powerOf10*digitList[k]
            powerOf10 = powerOf10*10
        return totalNumber
    def test_primalityCheck1(self):
        self.assertTrue(self.primalityTest(2))
    def test_primalityCheck2(self):
        self.assertTrue(self.primalityTest(3))
    def test_primalityCheck3(self):
        self.assertTrue(self.primalityTest(5))
    def test_primalityCheck4(self):
        self.assertTrue(self.primalityTest(7))
    def test_primalityCheck5(self):
        self.assertTrue(self.primalityTest(11))
    def test_primalityCheck6(self):
        self.assertTrue(self.primalityTest(37))
    def test_primalityCheck7(self):
        self.assertFalse(self.primalityTest(30))
    def test_primalityCheck8(self):
        self.assertFalse(self.primalityTest(21))
    def test_primalityCheck9(self):
        self.assertFalse(self.primalityTest(70))
    def test_primalityCheck10(self):
        self.assertFalse(self.primalityTest(111))
    def test_numberOfDigitCheck1(self):
        self.assertTrue(self.numberOfDigits(1) == 1)
    def test_numberOfDigitCheck2(self):
        self.assertTrue(self.numberOfDigits(10) == 2)
    def test_numberOfDigitCheck3(self):
        self.assertTrue(self.numberOfDigits(100) == 3)
    def test_numberOfDigitCheck4(self):
        self.assertTrue(self.numberOfDigits(1000) == 4)
    def test_numberOfDigitCheck5(self):
        self.assertTrue(self.numberOfDigits(2) == 1)
    def test_numberOfDigitCheck6(self):
        self.assertTrue(self.numberOfDigits(30) == 2)
    def test_numberOfDigitCheck7(self):
        self.assertTrue(self.numberOfDigits(400) == 3)
    def test_numberOfDigitCheck8(self):
        self.assertTrue(self.numberOfDigits(5000) == 4)
    def test_numberOfDigitCheck9(self):
        self.assertTrue(self.numberOfDigits(12314221) == 8)
    def test_numberOfDigitCheck10(self):
        self.assertTrue(self.numberOfDigits(123123) == 6)
    def test_listOfDigitsExample1(self):
        self.assertEqual(
            self.listOfDigits(123123),
            [1, 2, 3, 1, 2, 3]
            )
    def test_listOfDigitsExample2(self):
        self.assertEqual(
            self.listOfDigits(12314221),
            [1, 2, 3, 1, 4, 2, 2, 1]
            )
    def test_listOfDigitsExample3(self):
        self.assertEqual(
            self.listOfDigits(12341234),
            [1, 2, 3, 4, 1, 2, 3, 4]
            )
    def test_listOfDigitsExample4(self):
        self.assertEqual(
            self.listOfDigits(400), [4, 0, 0]
            )
    def test_palindromeCheckExample1(self):
        self.assertFalse(self.palindromeDigitsCheck(1000))
    def test_palindromeCheckExample2(self):
        self.assertTrue(self.palindromeDigitsCheck(1001))
    def test_palindromeCheckExample3(self):
        self.assertTrue(self.palindromeDigitsCheck(169961))
    def test_numberFromDigitsExample1(self):
        self.assertEqual(
            self.numberFormedFromDigitList(
                [1, 2, 2, 3, 4]
                ), 12234
            )
    def test_numberFromDigitsExample2(self):
        self.assertEqual(
            self.numberFormedFromDigitList(
                [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
                ), 1234512345
            )
    def test_numberFromDigitsExample3(self):
        self.assertEqual(
            self.numberFormedFromDigitList([1]), 1
            )
    def test_numberFromDigitsExample4(self):
        self.assertEqual(
            self.numberFormedFromDigitList([0, 1]), 1
            )
    def test_numberFromDigitsExample5(self):
        self.assertEqual(
            self.numberFormedFromDigitList([1, 0, 1]), 101
            )
    def test_numberFromDigitsExample6(self):
        self.assertEqual(
            self.numberFormedFromDigitList([1, 2, 3, 4]), 1234
            )
    def test_numberFromDigitsExample7(self):
        self.assertEqual(
            self.numberFormedFromDigitList([0]), 0
            )
    def test_numberFromDigitsExample8(self):
        self.assertEqual(
            self.numberFormedFromDigitList([0, 0]), 0
            )
    def test_reversiblePrimeSquareMain(self):
        print()
        nMaxRange = 5*10**7
        # 2*10**7 # 85*10**5 # 8*10**6 # 75*10**5
        # 7*10**6 # 65*10**5 # 6*10**6 # 55*10**5
        # 5*10**6 # 3*10**6 # 25*10**5
        # 2*10**6 # 15*10**5 # 10**6
        primeNumberBufferList = []
        for k in range(2, nMaxRange+1):
            if self.primalityTest(k):
                primeNumberBufferList.append(k)
        numberOfPrimes = len(primeNumberBufferList)
        primeNumberSquare = [
            primeNumberBufferList[k]**2 for k in range(numberOfPrimes)
            ]
        visitPrimeFlag = {}
        for k in range(numberOfPrimes):
            visitPrimeFlag[primeNumberSquare[k]] = False
        countReversiblePrimeSquare = 0
        for k in range(numberOfPrimes):
            reversiblePrimeSquare = primeNumberSquare[k]
            if not(visitPrimeFlag[reversiblePrimeSquare]):
                notPalindromePrimeSquare = not(self.palindromeDigitsCheck(reversiblePrimeSquare))
                firstBufferDigitList = self.listOfDigits(reversiblePrimeSquare)
                bufferNumberOfDigits = len(firstBufferDigitList)
                secondBufferDigitList = [firstBufferDigitList[k] for k in range(bufferNumberOfDigits)]
                secondBufferDigitList.reverse()
                secondReversiblePrimeSquare = self.numberFormedFromDigitList(secondBufferDigitList)
                if notPalindromePrimeSquare and secondReversiblePrimeSquare in visitPrimeFlag:
                    visitPrimeFlag[reversiblePrimeSquare] = True
                    visitPrimeFlag[secondReversiblePrimeSquare] = True
                    countReversiblePrimeSquare = countReversiblePrimeSquare + 2
        print("-"*40)
        print(
            "Number of reversible prime squares = ", countReversiblePrimeSquare
            )
        print("-"*40)
        sumOfReversiblePrimeSquares = 0
        listOfReversiblePrimeSquares = [
            169, 961, 12769, 96721, 1042441,
            1062961, 1216609, 1442401, 1692601, 9066121,
            121066009, 900660121, 12148668841, 12367886521, 12568876321,
            14886684121, 1000422044521, 1002007006009, 1020506060401, 1040606050201,
            1210684296721, 1212427816609, 1212665666521, 1214648656321, 1234367662441,
            1236568464121, 1254402240001, 1256665662121, 1276924860121, 1442667634321,
            9006007002001, 9066187242121, 100042424498641, 100222143232201, 100240164024001,
            100402824854641, 100420461042001, 102012282612769, 102014060240401, 102232341222001,
            104042060410201, 121002486012769, 121264386264121, 123212686214641, 146412686212321,
            146458428204001, 146894424240001, 967210684200121, 967216282210201
            ]
        listOfReversiblePrimes = [
            13, 31, 113, 311, 1021,
            1031, 1103, 1201, 1301, 3011,
            11003, 30011, 110221, 111211, 112111,
            122011, 1000211, 1001003, 1010201, 1020101,
            1100311, 1101103, 1101211, 1102111, 1111021,
            1112011, 1120001, 1121011, 1130011, 1201111,
            3001001, 3011011, 10002121, 10011101, 10012001,
            10020121, 10021001, 10100113, 10100201, 10111001,
            10200101, 11000113, 11012011, 11100121, 12100111,
            12102001, 12120001, 31100011, 31100101
            ]
        for reversiblePrimeSquare in visitPrimeFlag:
            if visitPrimeFlag[reversiblePrimeSquare]:
                sumOfReversiblePrimeSquares = sumOfReversiblePrimeSquares + reversiblePrimeSquare
                reversiblePrime = math.floor(math.sqrt(reversiblePrimeSquare))
                if self.primalityTest(reversiblePrime):
                    self.assertTrue(reversiblePrimeSquare in listOfReversiblePrimeSquares)
                    self.assertTrue(reversiblePrime in listOfReversiblePrimes)
        self.assertTrue(sumOfReversiblePrimeSquares == 3807504276997394)
if __name__ == "__main__":
    unittest.main()