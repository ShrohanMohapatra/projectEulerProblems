# ProjectEulerProblem33.py

import unittest

class test_ProjectEulerProblem33(unittest.TestCase):
    def cancellableFractionTwoDigits(self, x1, x2):
        x1Digits = [x1 // 10, x1 % 10]
        x2Digits = [x2 // 10, x2 % 10]
        if x1Digits[0] == x2Digits[0]:
            if x2Digits[1] == 0: return False
            return abs(x1/x2 - x1Digits[1]/x2Digits[1]) < 1.e-6
        elif x1Digits[0] == x2Digits[1]:
            if x2Digits[0] == 0: return False
            return abs(x1/x2 - x1Digits[1]/x2Digits[0]) < 1.e-6
        elif x1Digits[1] == x2Digits[0]:
            if x2Digits[1] == 0: return False
            return abs(x1/x2 - x1Digits[0]/x2Digits[1]) < 1.e-6
        elif x1Digits[1] == x2Digits[1]:
            if x2Digits[0] == 0: return False
            return abs(x1/x2 - x1Digits[0]/x2Digits[0]) < 1.e-6
        else:
            return False
    def nonTrivialCancellableFraction(self):
        numeratorList = []
        denominatorList = []
        for x1 in range(10, 99):
            for x2 in range(x1+1, 100):
                if self.cancellableFractionTwoDigits(x1, x2):
                    if x1%10 != 0 and x2%10 != 0:
                        numeratorList.append(x1)
                        denominatorList.append(x2)
        return {
            "Set of numerators": numeratorList,
            "Set of denominators": denominatorList
            }
    def test_cancellableFractionCheckV1(self):
        self.assertTrue(
            self.cancellableFractionTwoDigits(49, 98)
            )
    def test_cancellableFractionCheckV2(self):
        self.assertTrue(
            self.cancellableFractionTwoDigits(30, 50)
            )
    def test_cancellableFractionCheckV3(self):
        self.assertTrue(
            self.cancellableFractionTwoDigits(40, 50)
            )
    def test_cancellableFractionCheckV4(self):
        self.assertTrue(
            self.cancellableFractionTwoDigits(10, 50)
            )
    def test_cancellableFractionCheckV5(self):
        self.assertTrue(
            self.cancellableFractionTwoDigits(20, 50)
            )
    def test_cancellableFractionCheckV6(self):
        self.assertFalse(
            self.cancellableFractionTwoDigits(33, 63)
            )
    def test_cancellableFractionCheckV7(self):
        self.assertFalse(
            self.cancellableFractionTwoDigits(83, 93)
            )
    def test_cancellableFractionCheckV8(self):
        self.assertFalse(
            self.cancellableFractionTwoDigits(38, 88)
            )
    def test_cancellableFractionCheckV9(self):
        self.assertFalse(
            self.cancellableFractionTwoDigits(33, 88)
            )
    def test_cancellableFractionCheckV10(self):
        self.assertFalse(
            self.cancellableFractionTwoDigits(17, 67)
            )
    def test_listOfNonTrivialCancellables(self):
        listOfFractions = self.nonTrivialCancellableFraction()
        self.assertEqual(
            listOfFractions["Set of numerators"],
            [16, 19, 26, 49]
            )
        self.assertEqual(
            listOfFractions["Set of denominators"],
            [64, 95, 65, 98]
            )
        productOfNumerators = 16*19*26*49
        productOfDenominators = 64*95*65*98
        lowestFractionDenominators = productOfDenominators//productOfNumerators
        self.assertTrue(lowestFractionDenominators == 100)

if __name__ == "__main__":
    unittest.main()
