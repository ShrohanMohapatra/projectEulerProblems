# ProjectEulerProblem37.jl

function primalityTest(x)
    if x == 1
        return false
    elseif x == 2 || x == 3
        return true
    end
    ceilSqrtX = ceil(sqrt(x))
    count = 1
    flagPrimality = true
    for k = 2:ceilSqrtX
        if rem(x, k) == 0
            flagPrimality = false
            break
        end
    end
    return flagPrimality
end

function testPrimalityCheckV1()
    @assert primalityTest(2)
end
function testPrimalityCheckV2()
    @assert primalityTest(3)
end
function testPrimalityCheckV3()
    @assert primalityTest(5)
end
function testPrimalityCheckV4()
    @assert primalityTest(89)
end
function testPrimalityCheckV5()
    @assert primalityTest(181)
end
function testPrimalityCheckV6()
    @assert !(primalityTest(12))
end
function testPrimalityCheckV7()
    @assert !(primalityTest(21))
end
function testPrimalityCheckV8()
    @assert !(primalityTest(9))
end
function testPrimalityCheckV9()
    @assert !(primalityTest(100))
end
function testPrimalityCheckV10()
    @assert !(primalityTest(80))
end

function numOfDigits(inputNumber)
    if inputNumber == 0 || inputNumber == 1
        return 1
    else
        flagPowerOf10 = true
        z = inputNumber
        countPowerOf10 = 1
        while z > 1
            if rem(z, 10) == 0
                z = div(z, 10)
                countPowerOf10 = countPowerOf10 + 1
            else
                return ceil(log10(inputNumber))
            end
        end
        return ceil(countPowerOf10)
    end
end

function testDigitCountCheck1()
    @assert numOfDigits(0) == 1
end
function testDigitCountCheck2()
    @assert numOfDigits(1) == 1
end
function testDigitCountCheck3()
    @assert numOfDigits(10) == 2
end
function testDigitCountCheck4()
    @assert numOfDigits(100) == 3
end
function testDigitCountCheck5()
    @assert numOfDigits(1000) == 4
end
function testDigitCountCheck6()
    @assert numOfDigits(10000) == 5
end
function testDigitCountCheck7()
    @assert numOfDigits(100000) == 6
end
function testDigitCountCheck8()
    @assert numOfDigits(1000000) == 7
end
function testDigitCountCheck8()
    @assert numOfDigits(123) == 3
end
function testDigitCountCheck9()
    @assert numOfDigits(456781235) == 9
end
function testDigitCountCheck10()
    @assert numOfDigits(120) == 3
end
function testDigitCountCheck11()
    @assert numOfDigits(750102) == 6
end

function listOfDigits(inputNumber)
    digitCount = Int(numOfDigits(inputNumber))
    digitList = zeros(Int128, 1, digitCount)
    z = inputNumber
    for k = 1:1:digitCount
        digitList[digitCount+1-k] = rem(z, 10)
        z = div(z, 10)
    end
    return digitList
end

function testDigitListCheck1()
    digitList = listOfDigits(120)
    flagVerif = digitList[1] == 1
    flagVerif = flagVerif && digitList[2] == 2
    flagVerif = flagVerif && digitList[3] == 0
    @assert flagVerif
end
function testDigitListCheck2()
    digitList = listOfDigits(31243242)
    flagVerif = digitList[1] == 3
    flagVerif = flagVerif && digitList[2] == 1
    flagVerif = flagVerif && digitList[3] == 2
    flagVerif = flagVerif && digitList[4] == 4
    flagVerif = flagVerif && digitList[5] == 3
    flagVerif = flagVerif && digitList[6] == 2
    flagVerif = flagVerif && digitList[7] == 4
    flagVerif = flagVerif && digitList[8] == 2
    @assert flagVerif
end
function testDigitListCheck3()
    digitList = listOfDigits(7880)
    flagVerif = digitList[1] == 7
    flagVerif = flagVerif && digitList[2] == 8
    flagVerif = flagVerif && digitList[3] == 8
    flagVerif = flagVerif && digitList[4] == 0
    @assert flagVerif
end

function createNumber(listOfDigits)
    numberOfDigits = length(listOfDigits)
    powerOf10 = 1
    actualNumber = 0
    for k = 1:1:numberOfDigits
        actualNumber = actualNumber + powerOf10*listOfDigits[numberOfDigits+1-k]
        powerOf10 = powerOf10 * 10
    end
    return actualNumber
end

function testNumberFromDigitsFormationV1()
    @assert createNumber([1]) == 1
end
function testNumberFromDigitsFormationV2()
    @assert createNumber([1, 2]) == 12
end
function testNumberFromDigitsFormationV3()
    @assert createNumber([2, 1]) == 21
end
function testNumberFromDigitsFormationV4()
    @assert createNumber([5, 6, 7, 8, 7, 2, 3]) == 5678723
end
function testNumberFromDigitsFormationV5()
    @assert createNumber([9, 7, 8, 4, 3, 5, 2, 1, 6]) == 978435216
end

function truncatableCheck(inputPrime)
    digitCount = Int(numOfDigits(inputPrime))
    digitList = listOfDigits(inputPrime)
    flagVerif = true
    # if primalityTest(inputPrime)
    #     println("Truncated input prime = ", inputPrime)
    # end
    for k1 = 1:1:digitCount-1
        truncList = zeros(Int128, 1, k1)
        for k2 = 1:1:k1
            truncList[k2] = digitList[k2]
        end
        truncNumber = createNumber(truncList)
        flagVerif = flagVerif && primalityTest(truncNumber)
        # if primalityTest(truncNumber)
        #     println("Truncated prime = ", truncNumber)
        # end
        if !flagVerif
            return flagVerif
        end
    end
    for k1 = 2:1:digitCount
        truncList = zeros(Int128, 1, digitCount-k1+1)
        for k2 = k1:1:digitCount
            truncList[k2-k1+1] = digitList[k2]
        end
        truncNumber = createNumber(truncList)
        flagVerif = flagVerif && primalityTest(truncNumber)
        # if primalityTest(truncNumber)
        #     println("Truncated prime = ", truncNumber)
        # end
        if !flagVerif
            return flagVerif
        end
    end
    return flagVerif && primalityTest(inputPrime)
end

function testTruncatableCheck1()
    @assert primalityTest(3797) && truncatableCheck(3797)
end
function testTruncatableCheck2()
    @assert truncatableCheck(797)
end
function testTruncatableCheck3()
    @assert truncatableCheck(739397)
end

function mainDriverHandle()
    counter = 0
    sumOfPrimes = 0
    for x = 10:1:10^6
        if primalityTest(x)
            if truncatableCheck(x)
                counter = counter + 1
                println("(", counter, ") Truncatable prime ", x)
                sumOfPrimes = sumOfPrimes + x
            end
        end
    end
    println(string("Sum of all truncatable primes = ", sumOfPrimes))
    @assert counter == 11
    @assert sumOfPrimes == 748317
end

testPrimalityCheckV1()
testPrimalityCheckV2()
testPrimalityCheckV3()
testPrimalityCheckV4()
testPrimalityCheckV5()
testPrimalityCheckV6()
testPrimalityCheckV7()
testPrimalityCheckV8()
testPrimalityCheckV9()
testPrimalityCheckV10()

testDigitCountCheck1()
testDigitCountCheck2()
testDigitCountCheck3()
testDigitCountCheck4()
testDigitCountCheck5()
testDigitCountCheck6()
testDigitCountCheck7()
testDigitCountCheck8()
testDigitCountCheck9()
testDigitCountCheck10()
testDigitCountCheck11()

testDigitListCheck1()
testDigitListCheck2()
testDigitListCheck3()

testNumberFromDigitsFormationV1()
testNumberFromDigitsFormationV2()
testNumberFromDigitsFormationV3()
testNumberFromDigitsFormationV4()
testNumberFromDigitsFormationV5()

# testTruncatableCheck1()

testTruncatableCheck1()
testTruncatableCheck2()
testTruncatableCheck3()

mainDriverHandle()