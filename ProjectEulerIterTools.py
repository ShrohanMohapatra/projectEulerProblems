# ProjectEulerIterTools.py

import unittest
import itertools

class test_ProjectEulerIterTools(unittest.TestCase):
	def test_iterToolsAccumulateV1(self):
		listWork = [1, 2, 3, 4, 5, 6]
		accumulateList = list(itertools.accumulate(listWork))
		predictedAccumulateList = [1, 3, 6, 10, 15, 21]
		self.assertTrue(accumulateList == predictedAccumulateList)
	def test_iterToolsAccumulateV2(self):
		tupleWork = (7, 5, 6, 7, 8, 9, 10)
		accumulateTuple = tuple(itertools.accumulate(tupleWork))
		predictedAccumulateTuple = (7, 12, 18, 25, 33, 42, 52)
		self.assertTrue(accumulateTuple == predictedAccumulateTuple)
	def test_iterToolsAccumulateV3(self):
		nestedListWork = [[3, 4], [4, 5, 6], [7, 5, 6], [7], [8, 9, 7]]
		accumNestedListWork = list(itertools.accumulate(nestedListWork))
		predictedAccumNestedListWork = [
			[3, 4],
			[3, 4, 4, 5, 6],
			[3, 4, 4, 5, 6, 7, 5, 6],
			[3, 4, 4, 5, 6, 7, 5, 6, 7],
			[3, 4, 4, 5, 6, 7, 5, 6, 7, 8, 9, 7]
			]
		self.assertTrue(accumNestedListWork == predictedAccumNestedListWork)
	def test_iterToolsAccumulateV4(self):
		nestedTupleWork = ((8, 9), (10, 5, 7), (5, 6, 7))
		accumNestedListWork = tuple(itertools.accumulate(nestedTupleWork))
		predictedAccumNestedListWork = (
			(8, 9),
			(8, 9, 10, 5, 7),
			(8, 9, 10, 5, 7, 5, 6, 7)
			)
		self.assertTrue(accumNestedListWork == predictedAccumNestedListWork)
	def test_iterToolsAccumulateV5(self):
		exampleStr = "ABCDEFGHIJ"
		accumListString = list(itertools.accumulate(exampleStr))
		expectedAccumListString = [
			"A", "AB", "ABC", "ABCD", "ABCDE",
			"ABCDEF", "ABCDEFG", "ABCDEFGH", "ABCDEFGHI", "ABCDEFGHIJ"
			]
		self.assertTrue(accumListString == expectedAccumListString)
	def test_iterToolsAccumulateV6(self):
		self.assertTrue(
			list(itertools.chain("ABC", "DEF")) == ["A", "B", "C", "D", "E", "F"]
			)
	def test_iterToolsAccumulateV7(self):
		self.assertTrue(
			"".join(list(itertools.chain("ABC", "DEF"))) == "ABCDEF"
			)
	def test_iterToolsAccumulateV8(self):
		listStr1 = "abcdefg"
		listStr2 = "gfedbca"
		listStr3 = "abcdef"
		listStr4 = "fedbca"
		self.assertTrue(
			"".join(list(itertools.chain(listStr1, listStr2, listStr3, listStr4))) == \
			listStr1 + listStr2 + listStr3 + listStr4
			)
	def test_iterToolsAccumulateV9(self):
		p = 1
		for k in itertools.count(10, 10):
			if k < 8000: p += 1
			else: break
		self.assertTrue(p == 800)
	def test_iterToolsAccumulateV10(self):
		listWork = [1, 2, 3, 4]
		listOfCombins = [
			list(combin) for combin in itertools.combinations(listWork, 2)
			]
		expectedListOfCombins = [
			[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]
			]
		flagVerif = True
		for combin in expectedListOfCombins:
			flagVerif = flagVerif and combin in listOfCombins
		self.assertTrue(flagVerif)
	def test_iterToolsAccumulateV11(self):
		listWork = [1, 2, 3, 4, 5]
		listOfCombins = [
			list(combin) for combin in itertools.combinations(listWork, 3)
			]
		expectedListOfCombins = [
			[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5],
			[1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]
			]
		flagVerif = True
		for combin in expectedListOfCombins:
			flagVerif = flagVerif and combin in listOfCombins
		self.assertTrue(flagVerif)

if __name__ == "__main__":
	unittest.main()
