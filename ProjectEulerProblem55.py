# ProjectEulerProblem55.py

import unittest
import math

class test_ProjectEulerProblem55(unittest.TestCase):
    def numberOfDigits(self, x):
        powerOfTen = 0
        z = x
        while z > 0:
            if z % 10 != 0 and z != 1:
                return math.ceil(math.log10(x))
            else:
                z = z//10
                powerOfTen = powerOfTen + 1
        return powerOfTen
    def listOfDigits(self, x):
        digitCount = self.numberOfDigits(x)
        digitList = [0 for k in range(digitCount)]
        z = x
        for k in range(digitCount-1, -1, -1):
            digitList[k] = z % 10
            z =  z // 10
        return digitList
    def palindromeCheck(self, x):
        digitCount = self.numberOfDigits(x)
        digitList = self.listOfDigits(x)
        digitNumberHalf = digitCount // 2
        boolePalindrome = True
        for k in range(digitNumberHalf):
            boolePalindrome = boolePalindrome and digitList[k] == digitList[digitCount-1-k]
            if not(boolePalindrome):
                break
        return boolePalindrome
    def digitalReverse(self, x):
        digitCount = self.numberOfDigits(x)
        digitList = self.listOfDigits(x)
        powerOfTen = 1
        newNumber = 0
        for k in range(digitCount):
            newNumber = newNumber + powerOfTen*digitList[k]
            powerOfTen = powerOfTen * 10
        return newNumber    
    def lychrelNumber(self, x):
        flagLychrel = True
        z = x
        for k in range(50):
            reverseZ = self.digitalReverse(z)
            booleAddPalindrome = self.palindromeCheck(z + reverseZ)
            if booleAddPalindrome:
                flagLychrel = False
                break
            z = z + reverseZ
        if flagLychrel:
            return [0, flagLychrel]
        else:
            return [k+1, flagLychrel]
    def countLychrelNumbers(self):
        desiredCount = 0
        for k in range(1, 10000):
            lychrelNumberCheck = self.lychrelNumber(k)
            if lychrelNumberCheck[1]:
                desiredCount = desiredCount + 1
        return desiredCount
    def test_digitCountTestV1(self):
        self.assertTrue(self.numberOfDigits(1) == 1)
    def test_digitCountTestV2(self):
        self.assertTrue(self.numberOfDigits(2) == 1)
    def test_digitCountTestV3(self):
        self.assertTrue(self.numberOfDigits(7) == 1)
    def test_digitCountTestV4(self):
        self.assertTrue(self.numberOfDigits(10) == 2)
    def test_digitCountTestV5(self):
        self.assertTrue(self.numberOfDigits(15) == 2)
    def test_digitCountTestV6(self):
        self.assertTrue(self.numberOfDigits(30) == 2)
    def test_digitCountTestV7(self):
        self.assertTrue(self.numberOfDigits(100) == 3)
    def test_digitCountTestV8(self):
        self.assertTrue(self.numberOfDigits(1000) == 4)
    def test_digitCountTestV9(self):
        self.assertTrue(self.numberOfDigits(423) == 3)
    def test_digitCountTestV10(self):
        self.assertTrue(self.numberOfDigits(50000) == 5)
    def test_digitListTestV1(self):
        self.assertTrue(self.listOfDigits(1) == [1])
    def test_digitListTestV2(self):
        self.assertTrue(self.listOfDigits(2) == [2])
    def test_digitListTestV3(self):
        self.assertTrue(self.listOfDigits(15) == [1, 5])
    def test_digitListTestV4(self):
        self.assertTrue(self.listOfDigits(30) == [3, 0])
    def test_digitListTestV5(self):
        self.assertTrue(self.listOfDigits(7381039432) == [7, 3, 8, 1, 0, 3, 9, 4, 3, 2])
    def test_digitListTestV6(self):
        self.assertTrue(self.listOfDigits(10000) == [1, 0, 0, 0, 0])
    def test_digitListTestV7(self):
        self.assertTrue(self.listOfDigits(423) == [4, 2, 3])
    def test_palindromeCheckV1(self):
        self.assertTrue(self.palindromeCheck(123321))
    def test_palindromeCheckV2(self):
        self.assertTrue(self.palindromeCheck(34543))
    def test_palindromeCheckV3(self):
        self.assertTrue(self.palindromeCheck(19691))
    def test_palindromeCheckV4(self):
        self.assertTrue(self.palindromeCheck(4554))
    def test_palindromeCheckV5(self):
        self.assertTrue(self.palindromeCheck(1025335201))
    def test_digitalReverseCheckV1(self):
        self.assertTrue(self.digitalReverse(1234) == 4321)
    def test_digitalReverseCheckV2(self):
        self.assertTrue(self.digitalReverse(4321) == 1234)
    def test_digitalReverseCheckV3(self):
        self.assertTrue(self.digitalReverse(1234534) == 4354321)
    def test_digitalReverseCheckV4(self):
        self.assertTrue(self.digitalReverse(1) == 1)
    def test_digitalReverseCheckV5(self):
        self.assertTrue(self.digitalReverse(12) == 21)
    def test_digitalReverseCheckV6(self):
        self.assertTrue(self.digitalReverse(712) == 217)
    def test_digitalReverseCheckV7(self):
        self.assertTrue(self.digitalReverse(111) == 111)
    def test_lychrelNumberV1(self):
        lychrelNumberCheck = self.lychrelNumber(349)
        self.assertFalse(lychrelNumberCheck[1])
        self.assertEqual(lychrelNumberCheck[0], 3)
    def test_lychrelNumberV2(self):
        lychrelNumberCheck = self.lychrelNumber(47)
        self.assertFalse(lychrelNumberCheck[1])
        self.assertEqual(lychrelNumberCheck[0], 1)
    def test_lychrelNumberV3(self):
        lychrelNumberCheck = self.lychrelNumber(4994)
        self.assertTrue(lychrelNumberCheck[1])
    def test_lychrelNumberV4(self):
        lychrelNumberCheck = self.lychrelNumber(121)
        self.assertFalse(lychrelNumberCheck[1])
        self.assertEqual(lychrelNumberCheck[0], 1)
    def test_LychrelCountCheck(self):
        self.assertTrue(self.countLychrelNumbers() == 249)
if __name__ == "__main__":
    unittest.main()