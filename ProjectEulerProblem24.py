# ProjectEulerProblem24.py

import unittest

class test_ProjectEulerProblem24(unittest.TestCase):
    def customFactorial(self, n):
        if n == 0: return 1
        else:
            return n*self.customFactorial(n-1)
    def listNthPermutation(self, n, lenList, inputList):
        if lenList == 1:
            return inputList
        else:
            lenListMinusOneFactorial = self.customFactorial(lenList-1)
            firstElem = inputList[n//lenListMinusOneFactorial]
            leftOverList = []
            for elem in inputList:
                if elem != firstElem:
                    leftOverList.append(elem)
            return [firstElem] + self.listNthPermutation(
                                n % lenListMinusOneFactorial,
                                lenList-1,
                                leftOverList
                                )
    def iterativeListNthPermutation(self, n, lenList, inputList):
        if lenList == 1:
            return inputList
        else:
            remainderLenList = lenList
            overallList = []
            bufferForN = n
            bufferForInputList = [elem for elem in inputList]
            while remainderLenList >= 1:
                remListMinusOneFactorial = self.customFactorial(remainderLenList-1)
                firstElem = bufferForInputList[bufferForN//remListMinusOneFactorial]
                leftOverList = []
                for elem in bufferForInputList:
                    if elem != firstElem:
                        leftOverList.append(elem)
                overallList.append(firstElem)
                bufferForInputList = [elem for elem in leftOverList]
                bufferForN = bufferForN % remListMinusOneFactorial
                remainderLenList = remainderLenList - 1
            return overallList
    def test_customFactorialExample1(self):
        self.assertTrue(self.customFactorial(2) == 2)
    def test_customFactorialExample2(self):
        self.assertTrue(self.customFactorial(3) == 6)
    def test_customFactorialExample3(self):
        self.assertTrue(self.customFactorial(4) == 24)
    def test_customFactorialExample4(self):
        self.assertTrue(self.customFactorial(5) == 120)
    def test_customFactorialExample5(self):
        self.assertTrue(self.customFactorial(6) == 720)
    def test_listNthPermutationExample1(self):
        inputList = [k for k in range(3)]
        indexPermutation = 1
        self.assertEqual(
            self.listNthPermutation(
                indexPermutation-1, 3, inputList
                ),
            [0, 1, 2]
            )
    def test_listNthPermutationExample2(self):
        inputList = [k for k in range(3)]
        indexPermutation = 2
        self.assertEqual(
            self.listNthPermutation(
                indexPermutation-1, 3, inputList
                ),
            [0, 2, 1]
            )
    def test_listNthPermutationExample3(self):
        inputList = [k for k in range(3)]
        indexPermutation = 3
        self.assertEqual(
            self.listNthPermutation(
                indexPermutation-1, 3, inputList
                ),
            [1, 0, 2]
            )
    def test_listNthPermutationExample4(self):
        inputList = [k for k in range(3)]
        indexPermutation = 4
        self.assertEqual(
            self.listNthPermutation(
                indexPermutation-1, 3, inputList
                ),
            [1, 2, 0]
            )
    def test_listNthPermutationExample5(self):
        inputList = [k for k in range(3)]
        indexPermutation = 5
        self.assertEqual(
            self.listNthPermutation(
                indexPermutation-1, 3, inputList
                ),
            [2, 0, 1]
            )
    def test_listNthPermutationExample6(self):
        inputList = [k for k in range(4)]
        indexPermutation = 11
        self.assertEqual(
            self.listNthPermutation(
                indexPermutation-1, 4, inputList
                ),
            [1, 3, 0, 2]
            )
    def test_listNthPermutationExample7(self):
        inputList = [k for k in range(4)]
        indexPermutation = 20
        self.assertEqual(
            self.listNthPermutation(
                indexPermutation-1, 4, inputList
                ),
            [3, 0, 2, 1]
            )
    def test_iterativeListNthPermutationExample1(self):
        inputList = [k for k in range(3)]
        indexPermutation = 1
        self.assertEqual(
            self.iterativeListNthPermutation(
                indexPermutation-1, 3, inputList
                ),
            [0, 1, 2]
            )
    def test_iterativeListNthPermutationExample2(self):
        inputList = [k for k in range(3)]
        indexPermutation = 2
        self.assertEqual(
            self.iterativeListNthPermutation(
                indexPermutation-1, 3, inputList
                ),
            [0, 2, 1]
            )
    def test_iterativeListNthPermutationExample3(self):
        inputList = [k for k in range(3)]
        indexPermutation = 3
        self.assertEqual(
            self.iterativeListNthPermutation(
                indexPermutation-1, 3, inputList
                ),
            [1, 0, 2]
            )
    def test_iterativeListNthPermutationExample4(self):
        inputList = [k for k in range(3)]
        indexPermutation = 4
        self.assertEqual(
            self.iterativeListNthPermutation(
                indexPermutation-1, 3, inputList
                ),
            [1, 2, 0]
            )
    def test_iterativeListNthPermutationExample5(self):
        inputList = [k for k in range(3)]
        indexPermutation = 5
        self.assertEqual(
            self.iterativeListNthPermutation(
                indexPermutation-1, 3, inputList
                ),
            [2, 0, 1]
            )
    def test_iterativeListNthPermutationExample6(self):
        inputList = [k for k in range(4)]
        indexPermutation = 11
        self.assertEqual(
            self.iterativeListNthPermutation(
                indexPermutation-1, 4, inputList
                ),
            [1, 3, 0, 2]
            )
    def test_iterativeListNthPermutationExample7(self):
        inputList = [k for k in range(4)]
        indexPermutation = 20
        self.assertEqual(
            self.iterativeListNthPermutation(
                indexPermutation-1, 4, inputList
                ),
            [3, 0, 2, 1]
            )
    def test_iterativeListNthPermutationMainCase(self):
        inputList = [k for k in range(10)]
        indexPermutation = 1000000 # One million = 1,000,000
        self.assertEqual(
            self.iterativeListNthPermutation(
                indexPermutation-1, 10, inputList
                ),
            [2, 7, 8, 3, 9, 1, 5, 4, 6, 0]
            )


if __name__ == "__main__":
    unittest.main()
