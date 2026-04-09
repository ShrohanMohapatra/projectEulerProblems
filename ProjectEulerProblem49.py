# ProjectEulerProblem49.py

import unittest
import math

class test_ProjectEulerProblem49(unittest.TestCase):
    def gcdFinder(self, a, b):
        if a > b: return self.gcdFinder(b, a)
        elif b%a == 0: return a
        else: return self.gcdFinder(b%a, a)
    def perfectPowerCheck(self, n):
        ceilSqrtX = math.ceil(math.sqrt(n))
        ceilSqrtX = math.ceil(math.sqrt(n))
        for a in range(2, ceilSqrtX+1):
            exponentForA = 0
            zNumber = n
            while zNumber % a == 0:
                zNumber = zNumber // a
                exponentForA = exponentForA + 1
            aPowerB = 1
            for k in range(exponentForA):
                aPowerB = a*aPowerB
            if aPowerB == n:
                return {"TruthVal": True, "a": a, "exponentForA": exponentForA}
        return {"TruthVal": False, "a": 0, "exponentForA": 0}
    def customMultiplicativeOrder(self, n, a):
        p = a
        for k in range(1, 1001):
            if p % n == 1: return k
            else: p = p * a
    def eulerTotientFunction(self, n):
        countCoPrime = 0
        for k in range(1, n):
            if self.gcdFinder(n, k) == 1:
                countCoPrime = countCoPrime + 1
        return countCoPrime
    # Polynomial division
    def positiveIntegerDivisionModulo(self, a, b, n):
        # Here I try to look for the least positive
        # integer m possible for which
        # q = (m n + a)/b
        # is a positive integer modulo n.
        # 
        # I want to check if
        # [|a - b q|/n] == m mod n
        for m in range(1, b):
            if (m*n + a) % b == 0:
                break
        q = (m*n + a) // b
        self.assertTrue((abs(a-b*q))%n == 0)
        self.assertTrue((abs(a-b*q))//n == m)
        return {"Quotient": q, "Remainder": m%n}
    def rationalFieldPolynomialAdd(self, polyn1, polyn2):
        degPolyn1 = len(polyn1)-1
        degPolyn2 = len(polyn2)-1
        if degPolyn1 == degPolyn2:
            newPolynAdd = [{"Numerator": 0, "Denominator": 0} for k in range(degPolyn1+1)]
            for k in range(degPolyn1+1):
                gcdOfDenominators = self.gcdFinder(polyn1[k]["Denominator"], polyn2[k]["Denominator"])
                lcmOfDenominators = polyn1[k]["Denominator"]*polyn2[k]["Denominator"]//gcdOfDenominators
                newPolynAdd[k]["Denominator"] = lcmOfDenominators
                newPolynAdd[k]["Numerator"] = polyn1[k]["Numerator"]*polyn2[k]["Denominator"]//gcdOfDenominators + polyn2[k]["Numerator"]*polyn1[k]["Denominator"]//gcdOfDenominators
            return newPolynAdd
        elif degPolyn1 < degPolyn2:
            newPolynAdd = [{"Numerator": 0, "Denominator": 0} for k in range(degPolyn2+1)]
            for k in range(degPolyn1+1):
                gcdOfDenominators = self.gcdFinder(polyn1[k]["Denominator"], polyn2[k]["Denominator"])
                lcmOfDenominators = polyn1[k]["Denominator"]*polyn2[k]["Denominator"]//gcdOfDenominators
                newPolynAdd[k]["Denominator"] = lcmOfDenominators
                newPolynAdd[k]["Numerator"] = polyn1[k]["Numerator"]*polyn2[k]["Denominator"]//gcdOfDenominators + polyn2[k]["Numerator"]*polyn1[k]["Denominator"]//gcdOfDenominators
            for k in range(degPolyn1+1, degPolyn2+1):
                newPolynAdd[k]["Numerator"] = polyn2[k]["Numerator"]
                newPolynAdd[k]["Denominator"] = polyn2[k]["Denominator"]
            return newPolynAdd
        elif degPolyn1 > degPolyn2:
            newPolynAdd = [{"Numerator": 0, "Denominator": 0} for k in range(degPolyn1+1)]
            for k in range(degPolyn2+1):
                gcdOfDenominators = self.gcdFinder(polyn1[k]["Denominator"], polyn2[k]["Denominator"])
                lcmOfDenominators = polyn1[k]["Denominator"]*polyn2[k]["Denominator"]//gcdOfDenominators
                newPolynAdd[k]["Denominator"] = lcmOfDenominators
                newPolynAdd[k]["Numerator"] = polyn1[k]["Numerator"]*polyn2[k]["Denominator"]//gcdOfDenominators + polyn2[k]["Numerator"]*polyn1[k]["Denominator"]//gcdOfDenominators
            for k in range(degPolyn2+1, degPolyn1+1):
                newPolynAdd[k]["Numerator"] = polyn1[k]["Numerator"]
                newPolynAdd[k]["Denominator"] = polyn1[k]["Denominator"]
            return newPolynAdd
    def rationalFieldPolynomialDivision(self, polyn1, polyn2):
        # I assume p(x) = polyn1, d(x) = polyn2; deg(p(x)) >= deg(q(x))
        # I want to find q(x), r(x) such that p(x) = q(x) d(x) + r(x)
        # deg(q(x)) + deg(d(x)) = deg(p(x)); 0 <= deg(r(x)) < deg(p(x))
        degPolyn1 = len(polyn1)-1
        degPolyn2 = len(polyn2)-1
        rPolyn = [{} for k in range(degPolyn2)]
        qPolyn = [{} for k in range(degPolyn1-degPolyn2+1)]
        tempPpolyn = [polyn1[k] for k in range(degPolyn1+1)]
        tempRpolyn = [{} for k in range(degPolyn2)]
        for k in range(degPolyn2):
            rPolyn[k]["Numerator"] = 0
            rPolyn[k]["Denominator"] = 0
            tempRpolyn[k]["Numerator"] = 0
            tempRpolyn[k]["Denominator"] = 0
        for k in range(degPolyn1-degPolyn2+1):
            qPolyn[k]["Numerator"] = 0
            qPolyn[k]["Denominator"] = 0
        for k in range(degPolyn1-degPolyn2+1):
            targetNumerator = tempPpolyn[0]["Numerator"]*polyn2[0]["Denominator"]
            targetDenominator = tempPpolyn[0]["Denominator"]*polyn2[0]["Numerator"]
            gcdOfNumeratorDenominator = self.gcdFinder(targetNumerator, targetDenominator)
            qPolyn[k]["Numerator"] = targetNumerator//gcdOfNumeratorDenominator
            qPolyn[k]["Denominator"] = targetDenominator//gcdOfNumeratorDenominator
            
        return None
    def aksPrimalityTest(self, n):
        if self.perfectPowerCheck(n):
            return False
        else:
            rSmallest = 1
            ordRNlowerLimit = math.log2(n)*math.log2(n)
            for r in range(2, n):
                ordRN = self.customMultiplicativeOrder(r, n)
                if ordRN > ordRNlowerLimit:
                    rSmallest = r
                    break
            if self.gcdFinder(rSmallest, n) == 1:
                for a in range(2, min(rSmallest+1, n)):
                    if n % a == 0:
                        return False
                if n <= rSmallest:
                    return True
                else:
                    phiRsmallest = self.eulerTotientFunction(rSmallest)
                    logN = math.log2(n)
                    aMax = math.floor(phiRsmallest*logN)
                    # for a in range(1, aMax+1):
                    #     if (x+a)**n % (x**r - 1)
            else:
                return False
    def bufferListPrimeGen(self):
        self.assertTrue(True)
    def test_gcdTester1(self):
        self.assertEqual(self.gcdFinder(5, 6), 1)
    def test_gcdTester2(self):
        self.assertEqual(self.gcdFinder(5, 5), 5)
    def test_gcdTester3(self):
        self.assertEqual(self.gcdFinder(15, 5), 5)
    def test_gcdTester4(self):
        self.assertEqual(self.gcdFinder(24, 36), 12)
    def test_gcdTester5(self):
        self.assertEqual(self.gcdFinder(85, 119), 17)
    def test_gcdTester6(self):
        self.assertEqual(self.gcdFinder(8, 15), 1)
    def test_gcdTester7(self):
        self.assertEqual(self.gcdFinder(18, 24), 6)
    def test_PerfectPowerNumberCheck1(self):
        perfectPowerCertificate = self.perfectPowerCheck(1000)
        self.assertTrue(perfectPowerCertificate["TruthVal"])
        self.assertEqual(perfectPowerCertificate["a"], 10)
        self.assertEqual(perfectPowerCertificate["exponentForA"], 3)
    def test_PerfectPowerNumberCheck2(self):
        perfectPowerCertificate = self.perfectPowerCheck(64)
        self.assertTrue(perfectPowerCertificate["TruthVal"])
        self.assertEqual(perfectPowerCertificate["a"], 2)
        self.assertEqual(perfectPowerCertificate["exponentForA"], 6)
    def test_PerfectPowerNumberCheck3(self):
        perfectPowerCertificate = self.perfectPowerCheck(243)
        self.assertTrue(perfectPowerCertificate["TruthVal"])
        self.assertEqual(perfectPowerCertificate["a"], 3)
        self.assertEqual(perfectPowerCertificate["exponentForA"], 5)
    def test_PerfectPowerNumberCheck4(self):
        perfectPowerCertificate = self.perfectPowerCheck(65536)
        self.assertTrue(perfectPowerCertificate["TruthVal"])
        self.assertEqual(perfectPowerCertificate["a"], 2)
        self.assertEqual(perfectPowerCertificate["exponentForA"], 16)
    def test_PerfectPowerNumberCheck5(self):
        perfectPowerCertificate = self.perfectPowerCheck(108)
        self.assertFalse(perfectPowerCertificate["TruthVal"])
    def test_PerfectPowerNumberCheck6(self):
        perfectPowerCertificate = self.perfectPowerCheck(270)
        self.assertFalse(perfectPowerCertificate["TruthVal"])
    def test_PerfectPowerNumberCheck7(self):
        perfectPowerCertificate = self.perfectPowerCheck(26)
        self.assertFalse(perfectPowerCertificate["TruthVal"])
    def test_PerfectPowerNumberCheck8(self):
        perfectPowerCertificate = self.perfectPowerCheck(1849)
        self.assertTrue(perfectPowerCertificate["TruthVal"])
        self.assertEqual(perfectPowerCertificate["a"], 43)
        self.assertEqual(perfectPowerCertificate["exponentForA"], 2)
    def test_ordFunctionCheckCase1(self):
        self.assertEqual(self.gcdFinder(4, 7), 1)
        self.assertEqual(self.customMultiplicativeOrder(7, 4), 3)
    def test_ordFunctionCheckCase2(self):
        self.assertEqual(self.gcdFinder(3, 16), 1)
        self.assertEqual(self.customMultiplicativeOrder(16, 3), 4)
    def test_ordFunctionCheckCase3(self):
        self.assertEqual(self.gcdFinder(8, 15), 1)
        self.assertEqual(self.customMultiplicativeOrder(15, 8), 4)
    def test_ordFunctionCheckCase4(self):
        self.assertEqual(self.gcdFinder(5, 6), 1)
        self.assertEqual(self.customMultiplicativeOrder(6, 5), 2)
    def test_ordFunctionCheckCase5(self):
        self.assertEqual(self.gcdFinder(7, 10), 1)
        self.assertEqual(self.customMultiplicativeOrder(7, 10), 6)
    def test_eulerTotientFunctionCheckV1(self):
        self.assertEqual(self.eulerTotientFunction(5), 4)
    def test_eulerTotientFunctionCheckV2(self):
        self.assertEqual(self.eulerTotientFunction(12), 4)
    def test_eulerTotientFunctionCheckV3(self):
        self.assertEqual(self.eulerTotientFunction(28), 12)
    def test_eulerTotientFunctionCheckV4(self):
        self.assertEqual(self.eulerTotientFunction(35), 24)
    def test_eulerTotientFunctionCheckV5(self):
        self.assertEqual(self.eulerTotientFunction(72), 24)
    def test_positiveIntegerDivisionModularCongruenceCheckV1(self):
        divisionQuotientRemainder = self.positiveIntegerDivisionModulo(1, 13, 4)
        self.assertEqual(divisionQuotientRemainder["Quotient"], 1)
        self.assertEqual(divisionQuotientRemainder["Remainder"], 3)
    def test_positiveIntegerDivisionModularCongruenceCheckV2(self):
        divisionQuotientRemainder = self.positiveIntegerDivisionModulo(6, 13, 4)
        self.assertEqual(divisionQuotientRemainder["Quotient"], 2)
        self.assertEqual(divisionQuotientRemainder["Remainder"], 1)
    def test_positiveIntegerDivisionModularCongruenceCheckV3(self):
        divisionQuotientRemainder = self.positiveIntegerDivisionModulo(3, 17, 8)
        self.assertEqual(divisionQuotientRemainder["Quotient"], 3)
        self.assertEqual(divisionQuotientRemainder["Remainder"], 6)
    def test_positiveIntegerDivisionModularCongruenceCheckV4(self):
        divisionQuotientRemainder = self.positiveIntegerDivisionModulo(1, 5, 7)
        self.assertEqual(divisionQuotientRemainder["Quotient"], 3)
        self.assertEqual(divisionQuotientRemainder["Remainder"], 2)
    def test_positiveIntegerDivisionModularCongruenceCheckV5(self):
        divisionQuotientRemainder = self.positiveIntegerDivisionModulo(5, 6, 7)
        self.assertEqual(divisionQuotientRemainder["Quotient"], 2)
        self.assertEqual(divisionQuotientRemainder["Remainder"], 1)
    def test_positiveIntegerDivisionModularCongruenceCheckV6(self):
        divisionQuotientRemainder = self.positiveIntegerDivisionModulo(5, 3, 4)
        self.assertEqual(divisionQuotientRemainder["Quotient"], 3)
        self.assertEqual(divisionQuotientRemainder["Remainder"], 1)
    def test_positiveIntegerDivisionModularCongruenceCheckV7(self):
        divisionQuotientRemainder = self.positiveIntegerDivisionModulo(1, 3, 4)
        self.assertEqual(divisionQuotientRemainder["Quotient"], 3)
        self.assertEqual(divisionQuotientRemainder["Remainder"], 2)
    def test_rationalFieldPolynomialAddCheck1(self):
        polynomial1 = [
            {"Numerator": 3, "Denominator": 4},
            {"Numerator": 4, "Denominator": 5},
            {"Numerator": 7, "Denominator": 2},
            {"Numerator": 1, "Denominator": 8},
            {"Numerator": 1, "Denominator": 7}
            ]
        polynomial2 = [
            {"Numerator": 1, "Denominator": 2},
            {"Numerator": 7, "Denominator": 8},
            {"Numerator": 1, "Denominator": 3},
            {"Numerator": 1, "Denominator": 6},
            {"Numerator": 1, "Denominator": 6}
            ]
        polynomial3 = [
            {"Numerator": 5, "Denominator": 4},
            {"Numerator": 67, "Denominator": 40},
            {"Numerator": 23, "Denominator": 6},
            {"Numerator": 7, "Denominator": 24},
            {"Numerator": 13, "Denominator": 42}
            ]
        self.assertEqual(
            self.rationalFieldPolynomialAdd(
                polynomial1, polynomial2
                ), polynomial3
        )
    def test_rationalFieldPolynomialAddCheck2(self):
        polynomial1 = [
            {"Numerator": 3, "Denominator": 4},
            {"Numerator": 4, "Denominator": 5},
            {"Numerator": 7, "Denominator": 2},
            {"Numerator": 1, "Denominator": 8},
            {"Numerator": 1, "Denominator": 7}
            ]
        polynomial2 = [
            {"Numerator": 1, "Denominator": 2},
            {"Numerator": 7, "Denominator": 8},
            {"Numerator": 1, "Denominator": 3},
            {"Numerator": 1, "Denominator": 6},
            ]
        polynomial3 = [
            {"Numerator": 5, "Denominator": 4},
            {"Numerator": 67, "Denominator": 40},
            {"Numerator": 23, "Denominator": 6},
            {"Numerator": 7, "Denominator": 24},
            {"Numerator": 1, "Denominator": 7}
            ]
        self.assertEqual(
            self.rationalFieldPolynomialAdd(
                polynomial1, polynomial2
                ), polynomial3
        )
    def test_rationalFieldPolynomialAddCheck3(self):
        polynomial1 = [
            {"Numerator": 3, "Denominator": 4},
            {"Numerator": 4, "Denominator": 5},
            {"Numerator": 7, "Denominator": 2},
            {"Numerator": 1, "Denominator": 8}
            ]
        polynomial2 = [
            {"Numerator": 1, "Denominator": 2},
            {"Numerator": 7, "Denominator": 8},
            {"Numerator": 1, "Denominator": 3},
            {"Numerator": 1, "Denominator": 6},
            {"Numerator": 1, "Denominator": 6}
            ]
        polynomial3 = [
            {"Numerator": 5, "Denominator": 4},
            {"Numerator": 67, "Denominator": 40},
            {"Numerator": 23, "Denominator": 6},
            {"Numerator": 7, "Denominator": 24},
            {"Numerator": 1, "Denominator": 6}
            ]
        self.assertEqual(
            self.rationalFieldPolynomialAdd(
                polynomial1, polynomial2
                ), polynomial3
        )

if __name__ == "__main__":
    unittest.main()