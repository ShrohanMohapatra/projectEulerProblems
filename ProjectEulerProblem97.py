# ProjectEulerProblem97.py

import math

def numberOfDigits(x):
	return math.ceil(math.log10(x))

def listOfDigits(x):
	numDigs = numberOfDigits(x)
	returnList = [0 for k in range(numDigs)]
	z = x
	for k in range(numDigs-1, -1, -1):
		returnList[k] = z%10
		z = z//10
	return returnList


assert(numberOfDigits(12354) == 5)
assert(listOfDigits(1234153457) == [1, 2, 3, 4, 1, 5, 3, 4, 5, 7])

nonMersennePrime = 28433*2**(7830457) + 1
numDigsNonMersennePrime = numberOfDigits(nonMersennePrime)
assert(numDigsNonMersennePrime == 2357207)

A = [k for k in range(30)]
B1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
B2 = A[-10:]
assert(B1 == B2)
assert(len(B2) == 10)

listOfDigitsNonMersennePrime = [
	0 for k in range(numDigsNonMersennePrime)
	]

z = nonMersennePrime
for k in range(numDigsNonMersennePrime-1, numDigsNonMersennePrime-11, -1):
	listOfDigitsNonMersennePrime[k] = z%10
	z = z//10

assert(
	listOfDigitsNonMersennePrime[-10:] == [
		8, 7, 3, 9, 9, 9, 2, 5, 7, 7
		]
	)
