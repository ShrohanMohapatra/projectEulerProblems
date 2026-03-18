# ProjectEulerProblem50.jl

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

function knownCaseDriverFunction()
    maxPrimeCount = 10^4
    primeBools = falses(1, maxPrimeCount)
    for k = 1:maxPrimeCount
        primeBools[k] = primalityTest(k)
    end
    numberOfPrimes = 0
    for k = 1:maxPrimeCount
        if primeBools[k]
            numberOfPrimes = numberOfPrimes + 1
        end
    end
    listOfPrimes = zeros(Int128, 1, numberOfPrimes)
    m = 1
    for k = 1:maxPrimeCount
        if primeBools[k]
            listOfPrimes[m] = k
            m = m + 1
        end
    end
    @assert length(listOfPrimes) == numberOfPrimes
    maxConsecPrimes = 60
    maxSumPrimeCount = 1000
    listOfSumPrimeBools = falses(1, maxSumPrimeCount)
    numberOfConsecPrimesSum = zeros(Int128, 1, maxSumPrimeCount)
    for  index1 = 1:maxConsecPrimes
        for index2 = 1:numberOfPrimes-maxConsecPrimes
            sumConsecPrimes = 0
            for index3 = index2:index2+index1
                sumConsecPrimes = sumConsecPrimes + listOfPrimes[index3]
            end
            if sumConsecPrimes <= maxSumPrimeCount && primalityTest(sumConsecPrimes)
                listOfSumPrimeBools[sumConsecPrimes] = true
                storedMaxConsec = numberOfConsecPrimesSum[sumConsecPrimes]
                if storedMaxConsec <= index1
                    numberOfConsecPrimesSum[sumConsecPrimes] = index1+1
                end
            end
        end
    end
    sumWithMaxNumberConsecPrimes = argmax(numberOfConsecPrimesSum)[2]
    maxNumberConsecPrimes = maximum(numberOfConsecPrimesSum)
    @assert sumWithMaxNumberConsecPrimes == 953
    @assert maxNumberConsecPrimes == 21
end

function mainDriverFunction()
    maxPrimeCount = 10^5
    primeBools = falses(1, maxPrimeCount)
    for k = 1:maxPrimeCount
        primeBools[k] = primalityTest(k)
    end
    numberOfPrimes = 0
    for k = 1:maxPrimeCount
        if primeBools[k]
            numberOfPrimes = numberOfPrimes + 1
        end
    end
    listOfPrimes = zeros(Int128, 1, numberOfPrimes)
    m = 1
    for k = 1:maxPrimeCount
        if primeBools[k]
            listOfPrimes[m] = k
            m = m + 1
        end
    end
    @assert length(listOfPrimes) == numberOfPrimes
    println("-----------------------------------------------------")
    println("Max consecutive prime sum search until 1,000,000")
    println("-----------------------------------------------------")
    for k = 1:numberOfPrimes
        println(string("(", k, ") ", listOfPrimes[k]))
    end
    println("-----------------------------------------------------")
    maxConsecPrimes = 600 # 750 # 2000 # 1000 # 500
    maxSumPrimeCount = 10^6
    listOfSumPrimeBools = falses(1, maxSumPrimeCount)
    numberOfConsecPrimesSum = zeros(Int128, 1, maxSumPrimeCount)
    for  index1 = 1:maxConsecPrimes
        for index2 = 1:numberOfPrimes-maxConsecPrimes
            sumConsecPrimes = 0
            for index3 = index2:index2+index1
                sumConsecPrimes = sumConsecPrimes + listOfPrimes[index3]
            end
            if sumConsecPrimes <= maxSumPrimeCount && primalityTest(sumConsecPrimes)
                println(
                    string(
                        "The prime number ", sumConsecPrimes,
                        " can be expressed as ", index1+1, " consecutive primes."
                        )
                    )
                listOfSumPrimeBools[sumConsecPrimes] = true
                storedMaxConsec = numberOfConsecPrimesSum[sumConsecPrimes]
                if storedMaxConsec <= index1
                    numberOfConsecPrimesSum[sumConsecPrimes] = index1+1
                end
            end
        end
    end
    sumWithMaxNumberConsecPrimes = argmax(numberOfConsecPrimesSum)[2]
    maxNumberConsecPrimes = maximum(numberOfConsecPrimesSum)
    println("-----------------------------------------------------")
end

knownCaseDriverFunction()
mainDriverFunction()