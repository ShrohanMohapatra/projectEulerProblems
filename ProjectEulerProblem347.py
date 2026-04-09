# ProjectEulerProblem347.py

import unittest
import math

class test_ProjectEulerProblem347(unittest.TestCase):
    def primalityTest(self, x):
        if x == 1: return False
        elif x == 2 or x == 3: return True
        ceilSqrtX = math.ceil(math.sqrt(x))
        for k in range(2, ceilSqrtX+1):
            if x%k == 0:
                return False
        return True
    def bufferListOfPrimes(self, threshold):
        listOfPrimes = []
        for k in range(1, threshold+1):
            if self.primalityTest(k):
                listOfPrimes.append(k)
        return listOfPrimes
    def bufferListOfPrimesForMajorDriver(self, threshold):
        listOfPrimes = []
        for k in range(1, threshold+1):
            if self.primalityTest(k):
                print("> Prime number "+str(k))
                listOfPrimes.append(k)
        return listOfPrimes
    def largestIntegerDivPandQ(self, p, q, N):
        bufferPrimes = self.bufferListOfPrimes(N+1)
        flagDivisiblePrimes = {}
        for prime in bufferPrimes:
            flagDivisiblePrimes[prime] = False
        largestInt = 0
        for numberHunt in range(N, 0, -1):
            for prime in bufferPrimes:
                if numberHunt % prime == 0:
                    flagDivisiblePrimes[prime] = True
            if flagDivisiblePrimes[p] and flagDivisiblePrimes[q]:
                flagExclusivePrime = False
                for prime in bufferPrimes:
                    if flagDivisiblePrimes[prime] and prime!=p and prime!=q:
                        flagExclusivePrime = True
                        break
                if not(flagExclusivePrime):
                    largestInt = numberHunt
                    break
            for prime in bufferPrimes:
                flagDivisiblePrimes[prime] = False
        return largestInt
    def SfunctionDivPandQsmallCheck(self, inputNum):
        primesBufferList = self.bufferListOfPrimes(inputNum)
        numberOfPrimes = len(primesBufferList)
        dictLargestPowers = {}
        for primeNumber in primesBufferList:
            powerOfPrimeNumber = 0
            dummyVar = inputNum
            while dummyVar >= 1:
                dummyVar = dummyVar // primeNumber
                powerOfPrimeNumber = powerOfPrimeNumber + 1
            dictLargestPowers[primeNumber] = powerOfPrimeNumber
        dictLargestIntegerMultiple = {}
        for k in range(numberOfPrimes-1):
            dictLargestIntegerMultiple[primesBufferList[k]] = {}
            for m in range(k+1, numberOfPrimes):
                dictLargestIntegerMultiple[primesBufferList[k]][primesBufferList[m]] = 0
        sumOfLargestIntegerMultiple = 0
        for subSetPrimesLevel1 in dictLargestIntegerMultiple:
            for subSetPrimesLevel2 in dictLargestIntegerMultiple[subSetPrimesLevel1]:
                largestPowerSubSetPrime1 = dictLargestPowers[subSetPrimesLevel1]
                largestPowerSubSetPrime2 = dictLargestPowers[subSetPrimesLevel2]
                bufferArrPrimeMultiple = [
                    [0 for m in range(1, largestPowerSubSetPrime2+1)]
                        for k in range(1, largestPowerSubSetPrime1+1)
                        ]
                powerOfPrime1 = subSetPrimesLevel1
                for k in range(1, largestPowerSubSetPrime1+1):
                    powerOfPrime2 = subSetPrimesLevel2
                    for m in range(1, largestPowerSubSetPrime2+1):
                        contestantProduct = powerOfPrime1*powerOfPrime2
                        if contestantProduct <= inputNum:
                            bufferArrPrimeMultiple[k-1][m-1] = contestantProduct
                        else:
                            bufferArrPrimeMultiple[k-1][m-1] = 0
                        powerOfPrime2 = powerOfPrime2*subSetPrimesLevel2
                    powerOfPrime1 = powerOfPrime1*subSetPrimesLevel1
                maxProduct = -1
                for k in range(largestPowerSubSetPrime1):
                    for m in range(largestPowerSubSetPrime2):
                        if maxProduct <= bufferArrPrimeMultiple[k][m]:
                            maxProduct = bufferArrPrimeMultiple[k][m]
                dictLargestIntegerMultiple[subSetPrimesLevel1][subSetPrimesLevel2] = maxProduct
                sumOfLargestIntegerMultiple = sumOfLargestIntegerMultiple + maxProduct
        return sumOfLargestIntegerMultiple
    def SfunctionDivPandQmainDriver(self):
        inputNum = 10**7
        primesBufferList = self.bufferListOfPrimesForMajorDriver(inputNum)
        numberOfPrimes = len(primesBufferList)
        dictLargestPowers = {}
        for primeNumber in primesBufferList:
            powerOfPrimeNumber = 0
            dummyVar = inputNum
            while dummyVar >= 1:
                dummyVar = dummyVar // primeNumber
                powerOfPrimeNumber = powerOfPrimeNumber + 1
            dictLargestPowers[primeNumber] = powerOfPrimeNumber
            print("dictLargestPowers["+str(primeNumber)+"] = "+str(powerOfPrimeNumber))
        dictLargestIntegerMultiple = {}
        for k in range(numberOfPrimes-1):
            dictLargestIntegerMultiple[primesBufferList[k]] = {}
            for m in range(k+1, numberOfPrimes):
                dictLargestIntegerMultiple[primesBufferList[k]][primesBufferList[m]] = 0
                print(
                    "> Largest integer multiple dict parsed until ",
                    "("+str(primesBufferList[k])+","+str(primesBufferList[m])+")"
                    )
        sumOfLargestIntegerMultiple = 0
        for subSetPrimesLevel1 in dictLargestIntegerMultiple:
            for subSetPrimesLevel2 in dictLargestIntegerMultiple[subSetPrimesLevel1]:
                largestPowerSubSetPrime1 = dictLargestPowers[subSetPrimesLevel1]
                largestPowerSubSetPrime2 = dictLargestPowers[subSetPrimesLevel2]
                bufferArrPrimeMultiple = [
                    [0 for m in range(1, largestPowerSubSetPrime2+1)]
                        for k in range(1, largestPowerSubSetPrime1+1)
                        ]
                powerOfPrime1 = subSetPrimesLevel1
                for k in range(1, largestPowerSubSetPrime1+1):
                    powerOfPrime2 = subSetPrimesLevel2
                    for m in range(1, largestPowerSubSetPrime2+1):
                        contestantProduct = powerOfPrime1*powerOfPrime2
                        if contestantProduct <= inputNum:
                            bufferArrPrimeMultiple[k-1][m-1] = contestantProduct
                        else:
                            bufferArrPrimeMultiple[k-1][m-1] = 0
                        print(">> bufferArrPrimeMultiple["+str(k)+"]["+str(m)+"] = "+str(bufferArrPrimeMultiple[k-1][m-1]))
                        powerOfPrime2 = powerOfPrime2*subSetPrimesLevel2
                    powerOfPrime1 = powerOfPrime1*subSetPrimesLevel1
                maxProduct = -1
                print("-"*40)
                for k in range(largestPowerSubSetPrime1):
                    for m in range(largestPowerSubSetPrime2):
                        print(">>> bufferArrPrimeMultiple["+str(k)+"]["+str(m)+"] = "+str(bufferArrPrimeMultiple[k][m]))
                        if maxProduct <= bufferArrPrimeMultiple[k][m]:
                            maxProduct = bufferArrPrimeMultiple[k][m]
                print("-"*40)
                dictLargestIntegerMultiple[subSetPrimesLevel1][subSetPrimesLevel2] = maxProduct
                sumOfLargestIntegerMultiple = sumOfLargestIntegerMultiple + maxProduct
                print("-"*40)
                print("subSetPrimesLevel1 = ", subSetPrimesLevel1)
                print("subSetPrimesLevel2 = ", subSetPrimesLevel2)
                print(
                    "dictLargestIntegerMultiple[" + str(subSetPrimesLevel1) \
                    + "][" + str(subSetPrimesLevel2) \
                    + "] = " + str(maxProduct)
                    )
                print("-"*40)
        print("sumOfLargestIntegerMultiple =", sumOfLargestIntegerMultiple)
    def SfunctionDivPandQmainDriverVersion2(self):
        inputNum = 10**7
        primesBufferList = self.bufferListOfPrimesForMajorDriver(inputNum)
        numberOfPrimes = len(primesBufferList)
        dictLargestPowers = {}
        for primeNumber in primesBufferList:
            powerOfPrimeNumber = 0
            dummyVar = inputNum
            while dummyVar >= 1:
                dummyVar = dummyVar // primeNumber
                powerOfPrimeNumber = powerOfPrimeNumber + 1
            dictLargestPowers[primeNumber] = powerOfPrimeNumber
            print("dictLargestPowers["+str(primeNumber)+"] = "+str(powerOfPrimeNumber))
        dictLargestIntegerMultiple = {}
        sumOfLargestIntegerMultiple = 0
        for k in range(numberOfPrimes-1):
            dictLargestIntegerMultiple[primesBufferList[k]] = {}
            for m in range(k+1, numberOfPrimes):
                dictLargestIntegerMultiple[primesBufferList[k]][primesBufferList[m]] = 0
                print(
                    "> Largest integer multiple dict parsed until ",
                    "("+str(primesBufferList[k])+","+str(primesBufferList[m])+")"
                    )
                largestPowerSubSetPrime1 = dictLargestPowers[primesBufferList[k]]
                largestPowerSubSetPrime2 = dictLargestPowers[primesBufferList[m]]
                bufferArrPrimeMultiple = [
                    [0 for m in range(1, largestPowerSubSetPrime2+1)]
                        for k in range(1, largestPowerSubSetPrime1+1)
                        ]
                powerOfPrime1 = primesBufferList[k]
                for k1 in range(1, largestPowerSubSetPrime1+1):
                    powerOfPrime2 = primesBufferList[m]
                    for m1 in range(1, largestPowerSubSetPrime2+1):
                        contestantProduct = powerOfPrime1*powerOfPrime2
                        if contestantProduct <= inputNum:
                            bufferArrPrimeMultiple[k1-1][m1-1] = contestantProduct
                        else:
                            bufferArrPrimeMultiple[k1-1][m1-1] = 0
                        if bufferArrPrimeMultiple[k1-1][m1-1] != 0:
                            print(
                                ">> bufferArrPrimeMultiple["+str(k1)+"]["+str(m1)+"] = "+\
                                str(bufferArrPrimeMultiple[k1-1][m1-1])
                                )
                        powerOfPrime2 = powerOfPrime2*primesBufferList[m]
                    powerOfPrime1 = powerOfPrime1*primesBufferList[k]
                maxProduct = -1
                print("-"*40)
                for k1 in range(largestPowerSubSetPrime1):
                    for m1 in range(largestPowerSubSetPrime2):
                        if bufferArrPrimeMultiple[k1][m1] != 0:
                            print(
                                ">>> bufferArrPrimeMultiple["+str(k1)+"]["+str(m1)+"] = "+\
                                str(bufferArrPrimeMultiple[k1][m1])
                                )
                        if maxProduct <= bufferArrPrimeMultiple[k1][m1]:
                            maxProduct = bufferArrPrimeMultiple[k1][m1]
                print("-"*40)
                dictLargestIntegerMultiple[primesBufferList[k]][primesBufferList[m]] = maxProduct
                sumOfLargestIntegerMultiple = sumOfLargestIntegerMultiple + maxProduct
                print("-"*40)
                print("subSetPrimesLevel1 = ", primesBufferList[k])
                print("subSetPrimesLevel2 = ", primesBufferList[m])
                print(
                    "dictLargestIntegerMultiple[" + str(primesBufferList[k]) \
                    + "][" + str(primesBufferList[m]) \
                    + "] = " + str(maxProduct)
                    )
                print("-"*40)
        print("sumOfLargestIntegerMultiple =", sumOfLargestIntegerMultiple)
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
        self.assertFalse(self.primalityTest(15))
    def test_primalityTest7(self):
        self.assertFalse(self.primalityTest(30))
    def test_primalityTest8(self):
        self.assertFalse(self.primalityTest(9))
    def test_primalityTest9(self):
        self.assertFalse(self.primalityTest(121))
    def test_primalityTest10(self):
        self.assertTrue(self.primalityTest(17))
    def test_bufferPrimeListGen(self):
        self.assertEqual(
            self.bufferListOfPrimes(100),
            [
                2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
                ]
            )
    def test_largestIntPrimeMfunctionTest1(self):
        self.assertTrue(self.largestIntegerDivPandQ(2, 3, 100) == 96)
    def test_largestIntPrimeMfunctionTest2(self):
        self.assertTrue(self.largestIntegerDivPandQ(3, 5, 100) == 75)
    def test_largestIntPrimeMfunctionTest3(self):
        self.assertFalse(self.largestIntegerDivPandQ(2, 73, 100))
    def test_largestIntPrimeMfunctionTest4(self):
        self.assertTrue(self.largestIntegerDivPandQ(2, 5, 100) == 100)
    def test_sumLargestIntPrimesSmallDriverTest(self):
        self.assertTrue(self.SfunctionDivPandQsmallCheck(100) == 2262)
    # def test_sumLargestIntPrimesMajorDriverTest(self):
    #     print()
    #     print()
    #     self.SfunctionDivPandQmainDriver() # This function call generates a file >= 130 GB
    #     #Therefore, this approach is not recommended.
    #     self.assertTrue(True)
    # def test_sumLargestIntPrimesMajorDriverTest2(self):
    #     print()
    #     print()
    #     self.SfunctionDivPandQmainDriverVersion2() # This function call generates a file >= 130 GB
    #     # Therefore, this approach is not recommended.
    #     self.assertTrue(True)
if __name__ == "__main__":
    unittest.main()
