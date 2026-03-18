# ProjectEulerProblem65.py

import math

def convergentContinuedFraction(leadTermList, convNumberK):
    if convNumberK == 1:
        return {"numer": leadTermList[0], "denom": 1}
    elif convNumberK == 2:
        return {
            "numer": leadTermList[0]*leadTermList[1] + 1,
            "denom": leadTermList[1]
            }
    else:
        hNminusOne = leadTermList[0]*leadTermList[1] + 1
        kNminusOne = leadTermList[1]
        hNminusTwo = leadTermList[0]
        kNminusTwo = 1
        hN = 1
        kN = 0
        for k in range(3, convNumberK+1):
            hN = leadTermList[k-1]*hNminusOne + hNminusTwo
            kN = leadTermList[k-1]*kNminusOne + kNminusTwo
            hNminusTwo = hNminusOne
            kNminusTwo = kNminusOne
            hNminusOne = hN
            kNminusOne = kN
        return {"numer": hN, "denom": kN}

def numberOfDigits(x):
    z = x
    powOfTen = 1
    while z > 1:
        if z%10 != 0:
            return math.ceil(math.log10(x))
        else:
            z = z//10
            powOfTen = powOfTen + 1
    return powOfTen

def listOfDigits(x):
    digitCount = numberOfDigits(x)
    digitList = [0 for k in range(digitCount)]
    z = x
    for k in range(digitCount-1, -1, -1):
        digitList[k] = z % 10
        z = z // 10
    return digitList

def givenCaseDriver():
    leadTermList = [0 for k in range(100)]
    leadTermList[0] = 2
    leadTermList[1] = 1
    leadTermList[2] = 2
    for k in range(3, 100):
        if k % 3 == 2:
            leadTermList[k] = 2*((k + 1)//3)
        else:
            leadTermList[k] = 1
    convFraction = convergentContinuedFraction(leadTermList, 10)
    assert(sum(listOfDigits(convFraction["numer"])) == 17)

def mainProblemDriver():
    leadTermList = [0 for k in range(150)]
    leadTermList[0] = 2
    leadTermList[1] = 1
    leadTermList[2] = 2
    for k in range(3, 150):
        if k % 3 == 2:
            leadTermList[k] = 2*((k + 1)//3)
        else:
            leadTermList[k] = 1
    convFraction = convergentContinuedFraction(leadTermList, 100)
    assert(sum(listOfDigits(convFraction["numer"])) == 272)

givenCaseDriver()
mainProblemDriver()