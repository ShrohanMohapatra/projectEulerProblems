# ProjectEulerProblem49SimpleSolution.py

import unittest
import math

class test_ProjectEulerProblem49SimpleSolution(unittest.TestCase):
    def primalityTest(self, n):
        if n == 1: return False
        elif n == 2 or n == 3: return True
        else:
            ceilSqrtN = math.ceil(math.sqrt(n))
            for k in range(2, ceilSqrtN+1):
                if n % k == 0:
                    return False
            return True
    def numberOfDigits(self, n):
        boolePowerOf10 = True
        counterPowerOf10 = 0
        bufferForN = n
        while bufferForN > 1:
            if bufferForN % 10 != 0:
                boolePowerOf10 = False
                break
            else:
                counterPowerOf10 = counterPowerOf10 + 1
                bufferForN = bufferForN//10
        if boolePowerOf10:
            return counterPowerOf10 + 1
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
    def ifList1PermuteList2(self, list1, list2):
        dictOccurenceCountHash = {}
        for num1 in list1:
            if num1 not in dictOccurenceCountHash:
                dictOccurenceCountHash[num1] = 1
            else:
                dictOccurenceCountHash[num1] += 1
        for num2 in list2:
            if num2 not in dictOccurenceCountHash:
                return False
            else:
                dictOccurenceCountHash[num2] -= 1
        boolePermute = True
        for numIndex in dictOccurenceCountHash:
            boolePermute = boolePermute and not(dictOccurenceCountHash[numIndex])
            if not(boolePermute): return boolePermute
        return boolePermute
    def arithmeticProgressionCheck(self, a, b, c):
        return a + c == 2*b
    def fourDigitPrimePermutations(self):
        setOfPrimeAPs = {}
        counterPrimeArithmeticSequences = 0
        nDigitMax = 3
        baseListOfPrimes = []
        print()
        for k in range(10**nDigitMax, 10**(nDigitMax+1)):
            if self.primalityTest(k):
                baseListOfPrimes.append(k)
                print("> Prime encountered = ", k)
        numberOfFourDigitPrimes = len(baseListOfPrimes)
        for index1 in range(numberOfFourDigitPrimes-2):
            for index2 in range(index1+1, numberOfFourDigitPrimes-1):
                for index3 in range(index1+2, numberOfFourDigitPrimes):
                    a = baseListOfPrimes[index1]
                    b = baseListOfPrimes[index2]
                    c = baseListOfPrimes[index3]
                    booleArithmeticSequence = self.arithmeticProgressionCheck(a, b, c)
                    listOfDigitsInA = self.listOfDigits(a)
                    listOfDigitsInB = self.listOfDigits(b)
                    listOfDigitsInC = self.listOfDigits(c)
                    boolPermuteAB = self.ifList1PermuteList2(listOfDigitsInA, listOfDigitsInB)
                    boolPermuteAC = self.ifList1PermuteList2(listOfDigitsInA, listOfDigitsInC)
                    if a < b and b < c and booleArithmeticSequence and boolPermuteAB and boolPermuteAC:
                        print(">> True for a =", a, "b =", b, "c =", c, " out of", numberOfFourDigitPrimes, " primes.")
                        counterPrimeArithmeticSequences = counterPrimeArithmeticSequences + 1
                        setOfPrimeAPs[counterPrimeArithmeticSequences] = (a, b, c)
                        if counterPrimeArithmeticSequences >= 2:
                            return setOfPrimeAPs
                    # else: print(">> False for a =", a, "b =", b, "c =", c, " out of", numberOfFourDigitPrimes, " primes.")
    def test_primalityTest1(self):
        self.assertTrue(self.primalityTest(2))
    def test_primalityTest2(self):
        self.assertTrue(self.primalityTest(3))
    def test_primalityTest3(self):
        self.assertTrue(self.primalityTest(5))
    def test_primalityTest4(self):
        self.assertTrue(self.primalityTest(7))
    def test_primalityTest5(self):
        self.assertTrue(self.primalityTest(11))
    def test_primalityTest6(self):
        self.assertFalse(self.primalityTest(10))
    def test_primalityTest7(self):
        self.assertFalse(self.primalityTest(25))
    def test_primalityTest8(self):
        self.assertFalse(self.primalityTest(21))
    def test_numberOfDigitsCase1(self):
        self.assertTrue(self.numberOfDigits(1) == 1)
    def test_numberOfDigitsCase2(self):
        self.assertTrue(self.numberOfDigits(2) == 1)
    def test_numberOfDigitsCase3(self):
        self.assertTrue(self.numberOfDigits(5) == 1)
    def test_numberOfDigitsCase4(self):
        self.assertTrue(self.numberOfDigits(10) == 2)
    def test_numberOfDigitsCase5(self):
        self.assertTrue(self.numberOfDigits(100) == 3)
    def test_numberOfDigitsCase6(self):
        self.assertTrue(self.numberOfDigits(1000) == 4)
    def test_numberOfDigitsCase7(self):
        self.assertTrue(self.numberOfDigits(25) == 2)
    def test_numberOfDigitsCase8(self):
        self.assertTrue(self.numberOfDigits(1325) == 4)
    def test_listOfDigitsCase1(self):
        self.assertEqual(
            self.listOfDigits(12345),
            [1, 2, 3, 4, 5]
            )
    def test_listOfDigitsCase2(self):
        self.assertEqual(
            self.listOfDigits(1452785),
            [1, 4, 5, 2, 7, 8, 5]
            )
    def test_listOfDigitsCase3(self):
        self.assertEqual(
            self.listOfDigits(4152639),
            [4, 1, 5, 2, 6, 3, 9]
            )
    def test_listOfDigitsCase4(self):
        self.assertEqual(
            self.listOfDigits(963178745),
            [9, 6, 3, 1, 7, 8, 7, 4, 5]
            )
    def test_listOfDigitsCase5(self):
        self.assertEqual(
            self.listOfDigits(14256),
            [1, 4, 2, 5, 6]
            )
    def test_listOfDigitsCase6(self):
        self.assertEqual(
            self.listOfDigits(3178745),
            [3, 1, 7, 8, 7, 4, 5]
            )
    def test_listOfDigitsCase7(self):
        self.assertEqual(
            self.listOfDigits(145278523),
            [1, 4, 5, 2, 7, 8, 5, 2, 3]
            )
    def test_listOfDigitsCase8(self):
        self.assertEqual(
            self.listOfDigits(123123312),
            [1, 2, 3, 1, 2, 3, 3, 1, 2]
            )
    def test_listOfDigitsCase9(self):
        self.assertEqual(
            self.listOfDigits(1000000),
            [1, 0, 0, 0, 0, 0, 0]
            )
    def test_listPermuteExample1(self):
        self.assertTrue(
            self.ifList1PermuteList2([1], [1])
            )
    def test_listPermuteExample2(self):
        self.assertTrue(
            self.ifList1PermuteList2(
                [1, 2], [1, 2]
                )
            )
    def test_listPermuteExample3(self):
        self.assertTrue(
            self.ifList1PermuteList2(
                [1, 2], [2, 1]
                )
            )
    def test_listPermuteExample4(self):
        self.assertTrue(
            self.ifList1PermuteList2(
                [1, 2, 3], [2, 1, 3]
                )
            )
    def test_listPermuteExample5(self):
        self.assertFalse(
            self.ifList1PermuteList2(
                [1, 2, 3], [2, 1]
                )
            )
    def test_listPermuteExample6(self):
        self.assertFalse(
            self.ifList1PermuteList2(
                [1, 2, 3], [2, 1, 3, 1]
                )
            )
    def test_listPermuteExample7(self):
        self.assertFalse(
            self.ifList1PermuteList2(
                [1, 2, 3], [2, 1, 4, 1]
                )
            )
    def test_APCheckExample1(self):
        self.assertTrue(
            self.arithmeticProgressionCheck(1, 2, 3)
            )
    def test_APCheckExample2(self):
        self.assertTrue(
            self.arithmeticProgressionCheck(3, 2, 1)
            )
    def test_APCheckExample3(self):
        self.assertTrue(
            self.arithmeticProgressionCheck(1, 5, 9)
            )
    def test_APCheckExample4(self):
        self.assertTrue(
            self.arithmeticProgressionCheck(9, 5, 1)
            )
    def test_APCheckExample5(self):
        self.assertTrue(
            self.arithmeticProgressionCheck(1, -1, -3)
            )
    def test_APCheckExample6(self):
        self.assertTrue(
            self.arithmeticProgressionCheck(10, 25, 40)
            )
    def test_APCheckExample7(self):
        self.assertTrue(
            self.arithmeticProgressionCheck(1487, 4817, 8147)
            )
    def test_PrimeAPFourDigits(self):
        print(self.fourDigitPrimePermutations())
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
