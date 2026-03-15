# ProjectEulerProblem494.py

import unittest
import pprint

class test_ProjectEulerProblem494(unittest.TestCase):
	def collatzNextStep(self, x):
		if x%2:
			return 3*x + 1
		else: return x//2
	def boolPowerOf2(self, x):
		flagBool = True
		z = x
		while z > 1:
			if z%2:
				flagBool = False
				break
			else:
				z = z//2
		return flagBool
	def seqPrefix(self, x):
		seqList = [x]
		z = x
		while True:
			if self.boolPowerOf2(z):
				return seqList[:-1]
			else:
				z = self.collatzNextStep(z)
				seqList.append(z)
	def prefixFamilyCheck(self, A, B):
		nA = len(A)
		nB = len(B)
		flagVerif = nA == nB
		if not(flagVerif): return flagVerif
		for i in range(nA-1):
			for j in range(i+1, nA):
				flagVerif = flagVerif and (
					(A[i] >= A[j] or B[i] < B[j]) and \
					(B[i] >= B[j] or A[i] < A[j])
					)
		return flagVerif
	def distinctPrefixFamilySetList(self, listOfNumbers):
		maxSpan = 3*10**8
		# 10**8 # 5*10**7 # 3*10**7 # 10**7
		# 75*10**5 # 10**5 # 5*10**5 # 10**6 # 5*10**6
		dictPrefixFamily = {}
		for number in listOfNumbers:
			dictPrefixFamily[number] = []
		for x in range(3, maxSpan+1):
			seqPrefixForX = self.seqPrefix(x)
			for number in listOfNumbers:
				if len(seqPrefixForX) == number:
					nMemPrefixFamily = len(dictPrefixFamily[number])
					if nMemPrefixFamily == 0:
						dictPrefixFamily[number].append([seqPrefixForX])
					else:
						flagFindFamily = False
						for k in range(nMemPrefixFamily):
							extractedSetPrefixSequences = dictPrefixFamily[number][k]
							checkPrefixSeq = extractedSetPrefixSequences[0]
							flagFamilyMember = self.prefixFamilyCheck(seqPrefixForX, checkPrefixSeq)
							if flagFamilyMember:
								dictPrefixFamily[number][k].append(seqPrefixForX)
								flagFindFamily = True
								break
						if not(flagFindFamily):
							dictPrefixFamily[number].append([seqPrefixForX])
		return dictPrefixFamily
	def customPreprintThreeDimTensor(self, A):
		lengthFirstDimA = len(A)
		print("[")
		for k in range(lengthFirstDimA):
			lengthSecondDimA = len(A[k])
			print("\t[")
			for m in range(lengthSecondDimA):
				print("\t\t", A[k][m])
			print("\t]")
		print("]") 
	def test_powerOfTwoCheck1(self):
		self.assertTrue(self.boolPowerOf2(2))
	def test_powerOfTwoCheck2(self):
		self.assertTrue(self.boolPowerOf2(4))
	def test_powerOfTwoCheck3(self):
		self.assertTrue(self.boolPowerOf2(8))
	def test_powerOfTwoCheck4(self):
		self.assertFalse(self.boolPowerOf2(12))
	def test_powerOfTwoCheck5(self):
		self.assertFalse(self.boolPowerOf2(14))
	def test_powerOfTwoCheck6(self):
		self.assertFalse(self.boolPowerOf2(19))
	def test_collatzNextStepCheck1(self):
		self.assertTrue(self.collatzNextStep(100) == 50)
	def test_collatzNextStepCheck2(self):
		self.assertTrue(self.collatzNextStep(40) == 20)
	def test_collatzNextStepCheck3(self):
		self.assertTrue(self.collatzNextStep(15) == 46)
	def test_collatzNextStepCheck4(self):
		self.assertTrue(self.collatzNextStep(46) == 23)
	def test_collatzNextStepCheck5(self):
		self.assertTrue(self.collatzNextStep(23) == 70)
	def test_sequencePrefixCheckV1(self):
		self.assertTrue(self.seqPrefix(13) == [13, 40, 20, 10, 5])
	def test_sequencePrefixCheckV2(self):
		self.assertTrue(
			self.seqPrefix(15) == [
				15, 46, 23, 70, 35, 106,
				53, 160, 80, 40, 20, 10, 5
				]
			)
	def test_sequencePrefixCheckV3(self):
		self.assertTrue(self.seqPrefix(12) == [12, 6, 3, 10, 5])
	def test_sequencePrefixCheckV4(self):
		self.assertTrue(self.seqPrefix(8) == [])
	def test_sequencePrefixCheckV5(self):
		self.assertTrue(self.seqPrefix(16) == [])
	def test_sequencePrefixCheckV6(self):
		self.assertTrue(self.seqPrefix(454) == [454, 227, 682, 341])
	def test_sequencePrefixCheckV7(self):
		self.assertTrue(self.seqPrefix(113) == [113, 340, 170, 85])
	def test_sequencePrefixCheckV8(self):
		self.assertTrue(self.seqPrefix(6) == [6, 3, 10, 5])
	def test_prefixFamilyConfirmV1(self):
		self.assertTrue(
			self.prefixFamilyCheck(
				[6, 3, 10, 5], [454, 227, 682, 341]
				)
			)
	def test_prefixFamilyConfirmV2(self):
		self.assertFalse(
			self.prefixFamilyCheck(
				[454, 227, 682, 341], [113, 340, 170, 85]
				)
			)
	def test_distinctFamilySetCheck(self):
		inputList = [5, 10, 20, 90]
		prefixFamilyDict = self.distinctPrefixFamilySetList(inputList)
		for number in inputList:
			prefixFamilySet = prefixFamilyDict[number]
			lenPrefixFamilySet = len(prefixFamilyDict[number])
			print("-"*40)
			self.customPreprintThreeDimTensor(prefixFamilySet)
			print("-"*40)
			print("f("+str(number)+") =", lenPrefixFamilySet)
			print("-"*40)
		self.assertTrue(len(prefixFamilyDict[5]) == 5)

if __name__ == "__main__":
	unittest.main()