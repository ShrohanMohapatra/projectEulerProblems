# ProjectEulerProblemZero.py

sumOfSq = 0
numOfElems = 814000 # 7 # 6 # 5 # 814
numOfElemsBy2 = numOfElems//2
numOfSqNums = numOfElemsBy2 + 1 if numOfElems%2 == 1 else numOfElemsBy2
for k in range(numOfSqNums):
	print("("+str(k+1)+") Square number = ", (2*k+1)**2)
	sumOfSq += (2*k+1)**2
print(sumOfSq)
# assert(sumOfSq == 89892055)