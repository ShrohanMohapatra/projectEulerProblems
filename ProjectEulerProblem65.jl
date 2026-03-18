# ProjectEulerProblem65.jl

mutable struct rationalFraction
    numer :: Int128
    denom :: Int128 
end

function convergentContinuedFraction(leadTermList, convNumberK)
    if convNumberK == 1
        return rationalFraction(leadTermList[1], 1)
    elseif convNumberK == 2
        return rationalFraction(
            leadTermList[1]*leadTermList[2] + 1,
            leadTermList[2]
            )
    else
        hNminusOne = leadTermList[1]*leadTermList[2] + 1
        kNminusOne = leadTermList[2]
        hNminusTwo = leadTermList[1]
        kNminusTwo = 1
        hN = 1
        kN = 0
        for k = 3:convNumberK
            hN = leadTermList[k]*hNminusOne + hNminusTwo
            kN = leadTermList[k]*kNminusOne + kNminusTwo
            hNminusTwo = hNminusOne
            kNminusTwo = kNminusOne
            hNminusOne = hN
            kNminusOne = kN
        end
        return rationalFraction(hN, kN)
    end
end

function testConvergentFractionCheckV1()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 1
    for k = 2:1:100
        leadTermList[k] = 2
    end
    convFraction = convergentContinuedFraction(leadTermList, 1) 
    @assert convFraction.numer == 1
    @assert convFraction.denom == 1
end
function testConvergentFractionCheckV2()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 1
    for k = 2:1:100
        leadTermList[k] = 2
    end
    convFraction = convergentContinuedFraction(leadTermList, 2) 
    @assert convFraction.numer == 3
    @assert convFraction.denom == 2
end

function testConvergentFractionCheckV3()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 1
    for k = 2:1:100
        leadTermList[k] = 2
    end
    convFraction = convergentContinuedFraction(leadTermList, 3) 
    @assert convFraction.numer == 7
    @assert convFraction.denom == 5
end

function testConvergentFractionCheckV4()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 1
    for k = 2:1:100
        leadTermList[k] = 2
    end
    convFraction = convergentContinuedFraction(leadTermList, 4) 
    @assert convFraction.numer == 17
    @assert convFraction.denom == 12
end

function testConvergentFractionCheckV5()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 1
    for k = 2:1:100
        leadTermList[k] = 2
    end
    convFraction = convergentContinuedFraction(leadTermList, 5) 
    @assert convFraction.numer == 41
    @assert convFraction.denom == 29
end

function testConvergentFractionCheckV6()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 1
    for k = 2:1:100
        leadTermList[k] = 2
    end
    convFraction = convergentContinuedFraction(leadTermList, 7) 
    @assert convFraction.numer == 239
    @assert convFraction.denom == 169
end

function testConvergentFractionCheckV7()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 1
    for k = 2:1:100
        leadTermList[k] = 2
    end
    convFraction = convergentContinuedFraction(leadTermList, 10) 
    @assert convFraction.numer == 3363
    @assert convFraction.denom == 2378
end

function testConvergentFractionCheckV8()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 1) 
    @assert convFraction.numer == 2
    @assert convFraction.denom == 1
end

function testConvergentFractionCheckV9()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 2) 
    @assert convFraction.numer == 3
    @assert convFraction.denom == 1
end

function testConvergentFractionCheckV10()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 3) 
    @assert convFraction.numer == 8
    @assert convFraction.denom == 3
end

function testConvergentFractionCheckV11()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 4) 
    @assert convFraction.numer == 11
    @assert convFraction.denom == 4
end

function testConvergentFractionCheckV12()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 5) 
    @assert convFraction.numer == 19
    @assert convFraction.denom == 7
end

function testConvergentFractionCheckV13()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 6) 
    @assert convFraction.numer == 87
    @assert convFraction.denom == 32
end

function testConvergentFractionCheckV14()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 7) 
    @assert convFraction.numer == 106
    @assert convFraction.denom == 39
end

function testConvergentFractionCheckV15()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 8) 
    @assert convFraction.numer == 193
    @assert convFraction.denom == 71
end

function testConvergentFractionCheckV16()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 9) 
    @assert convFraction.numer == 1264
    @assert convFraction.denom == 465
end

function testConvergentFractionCheckV17()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 10) 
    @assert convFraction.numer == 1457
    @assert convFraction.denom == 536
end

function numberOfDigits(x)
    z = x
    powOf10 = 1
    while z > 1
        if rem(z, 10) != 0
            return Int(ceil(log10(x)))
        else
            z = div(z, 10)
            powOf10 = powOf10 + 1
        end
    end
    return powOf10
end

function testNumberOfDigitsCheckV1()
    @assert numberOfDigits(1) == 1
end
function testNumberOfDigitsCheckV2()
    @assert numberOfDigits(10) == 2
end
function testNumberOfDigitsCheckV3()
    @assert numberOfDigits(100) == 3
end
function testNumberOfDigitsCheckV4()
    @assert numberOfDigits(10112) == 5
end
function testNumberOfDigitsCheckV5()
    @assert numberOfDigits(10001) == 5
end
function testNumberOfDigitsCheckV6()
    @assert numberOfDigits(1456714567) == 10
end
function testNumberOfDigitsCheckV7()
    @assert numberOfDigits(1457) == 4
end

function listOfDigits(x)
    z = x
    kMax = numberOfDigits(x)
    returnList = zeros(Int128, 1, kMax)
    for k = kMax:-1:1
        returnList[k] = Int(rem(z, 10))
        z = Int(div(z, 10))
    end
    return returnList
end

function testDigitListCheckV1()
    digitList = listOfDigits(1230)
    @assert digitList[1] == 1
    @assert digitList[2] == 2
    @assert digitList[3] == 3
    @assert digitList[4] == 0
end

function testDigitListCheckV2()
    digitList = listOfDigits(100)
    @assert digitList[1] == 1
    @assert digitList[2] == 0
    @assert digitList[3] == 0
end

function testDigitListCheckV3()
    digitList = listOfDigits(65536)
    @assert digitList[1] == 6
    @assert digitList[2] == 5
    @assert digitList[3] == 5
    @assert digitList[4] == 3
    @assert digitList[5] == 6
end

function testDigitListCheckV4()
    digitList = listOfDigits(4294967296)
    @assert digitList[1] == 4
    @assert digitList[2] == 2
    @assert digitList[3] == 9
    @assert digitList[4] == 4
    @assert digitList[5] == 9
    @assert digitList[6] == 6
    @assert digitList[7] == 7
    @assert digitList[8] == 2
    @assert digitList[9] == 9
    @assert digitList[10] == 6
end

function testDigitListCheckV5()
    digitList = listOfDigits(2)
    @assert digitList[1] == 2
end

function givenCaseDriver()
    leadTermList = zeros(Int128, 1, 100)
    leadTermList[1] = 2
    leadTermList[2] = 1
    leadTermList[3] = 2
    for k = 4:1:100
        if rem(k, 3) == 0
            leadTermList[k] = 2*div(k, 3)
        else
            leadTermList[k] = 1
        end
    end
    convFraction = convergentContinuedFraction(leadTermList, 10)
    @assert sum(listOfDigits(convFraction.numer)) == 17
end

testConvergentFractionCheckV1()
testConvergentFractionCheckV2()
testConvergentFractionCheckV3()
testConvergentFractionCheckV4()
testConvergentFractionCheckV5()
testConvergentFractionCheckV6()
testConvergentFractionCheckV7()
testConvergentFractionCheckV8()
testConvergentFractionCheckV9()
testConvergentFractionCheckV10()
testConvergentFractionCheckV11()
testConvergentFractionCheckV12()
testConvergentFractionCheckV13()
testConvergentFractionCheckV14()
testConvergentFractionCheckV15()
testConvergentFractionCheckV16()
testConvergentFractionCheckV17()

testNumberOfDigitsCheckV1()
testNumberOfDigitsCheckV2()
testNumberOfDigitsCheckV3()
testNumberOfDigitsCheckV4()
testNumberOfDigitsCheckV5()
testNumberOfDigitsCheckV6()
testNumberOfDigitsCheckV7()

testDigitListCheckV1()
testDigitListCheckV2()
testDigitListCheckV3()
testDigitListCheckV4()
testDigitListCheckV5()

givenCaseDriver()