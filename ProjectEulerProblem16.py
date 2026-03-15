#ProjectEulerProblem16.py

stringNum = str(2**1000)
numOfDigits = len(stringNum)
print(sum([int(stringNum[k]) for k in range(numOfDigits)]))