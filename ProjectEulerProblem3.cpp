// ProjectEulerProblem3.cpp

#include<iostream>
#include<array>
#include<cmath>
#include<cassert>

using namespace std;

struct primeFactorMap{
    unsigned long long int primeFactor;
    unsigned long long int primeFactorExponent;
};

bool primalityTest(unsigned long long int p){
    if(p == 1){
        return false;
    }
    else{
        if(p == 2 || p == 3){
            return true;
        }
        else{
            unsigned long long int x;
            long double sqrtP = ceil(sqrt(static_cast<long double>(p)));
            unsigned long long int ceilSqrtP = static_cast<unsigned long long int>(sqrtP);
            bool targetVerifPrime = true;
            for(x = 2; x <= ceilSqrtP+1; x++){
                if(p % x == 0){
                    targetVerifPrime = false;
                    break;
                }
            }
            return targetVerifPrime;
        }
    }
}

array<primeFactorMap, 10000> primeFactorization(unsigned long long int x){
    array<unsigned long long int, 10000> bufferPrimeList;
    array<primeFactorMap, 10000> targetPrimeFactorMap;
    unsigned long long int indexCheck;
    unsigned long long int primeNumberCounter = 0;
    for(indexCheck = 2; indexCheck < x; indexCheck++){
        if(primalityTest(indexCheck)){
            bufferPrimeList[primeNumberCounter] = indexCheck;
            primeNumberCounter = primeNumberCounter + 1;
        }
    }
    unsigned long long int bufferForX = x;
    unsigned long long int primeIndex = 0;
    unsigned long long int bufferRepoIndex = 0;
    unsigned long long int bufferPrime;
    unsigned long long int factorCounter;
    while(bufferForX > 1){
        bufferPrime = bufferPrimeList[primeIndex];
        factorCounter = 0;
        while(bufferForX % bufferPrime == 0){
            bufferForX = bufferForX / bufferPrime;
            factorCounter = factorCounter + 1;
        }
        if(factorCounter >= 1){
            targetPrimeFactorMap[bufferRepoIndex].primeFactor =  bufferPrimeList[primeIndex];
            targetPrimeFactorMap[bufferRepoIndex].primeFactorExponent = factorCounter;
            bufferRepoIndex = bufferRepoIndex + 1;
        }
        primeIndex = primeIndex + 1;
    }
    return targetPrimeFactorMap;
}

array<primeFactorMap, 10000> primeFactorizationScaledUp(unsigned long long int x){
    array<unsigned long long int, 10000> bufferPrimeList;
    array<primeFactorMap, 10000> targetPrimeFactorMap;
    unsigned long long int indexCheck;
    unsigned long long int primeNumberCounter = 0;
    for(indexCheck = 2; indexCheck < x; indexCheck = indexCheck + 1){
        if(primalityTest(indexCheck)){
            bufferPrimeList[primeNumberCounter] = indexCheck;
            primeNumberCounter = primeNumberCounter + 1;
        }
        if(primeNumberCounter >= 10000){
            break;
        }
    }
    unsigned long long int bufferForX = x;
    unsigned long long int primeIndex = 0;
    unsigned long long int bufferRepoIndex = 0;
    unsigned long long int bufferPrime;
    unsigned long long int factorCounter;
    while(bufferForX > 1){
        bufferPrime = bufferPrimeList[primeIndex];
        factorCounter = 0;
        while(bufferForX % bufferPrime == 0){
            bufferForX = bufferForX / bufferPrime;
            factorCounter = factorCounter + 1;
        }
        if(factorCounter >= 1){
            targetPrimeFactorMap[bufferRepoIndex].primeFactor =  bufferPrimeList[primeIndex];
            targetPrimeFactorMap[bufferRepoIndex].primeFactorExponent = factorCounter;
            bufferRepoIndex = bufferRepoIndex + 1;
        }
        primeIndex = primeIndex + 1;
    }
    return targetPrimeFactorMap;
}

bool primalityTestExample1(){
    return primalityTest(2);
}
bool primalityTestExample2(){
    return primalityTest(3);
}
bool primalityTestExample3(){
    return primalityTest(5);
}
bool primalityTestExample4(){
    return primalityTest(7);
}
bool primalityTestExample5(){
    return primalityTest(11);
}
bool primalityTestExample6(){
    return primalityTest(17);
}
bool primalityTestExample7(){
    return primalityTest(83);
}
bool primalityTestExample8(){
    return primalityTest(20);
}
bool primalityTestExample9(){
    return primalityTest(4);
}
bool primalityTestExample10(){
    return primalityTest(9);
}
bool primalityTestExample11(){
    return primalityTest(25);
}
bool primalityTestExample12(){
    return primalityTest(12);
}
bool primalityTestExample13(){
    return primalityTest(35);
}
bool primalityTestExample14(){
    return primalityTest(120);
}

bool primeFactorizationExample1(){
    unsigned long long int xInput = 500;
    array<primeFactorMap, 10000> primeFactorsOfX = primeFactorization(xInput);
    bool flagVerif = primeFactorsOfX[0].primeFactor == 2;
    flagVerif = flagVerif && primeFactorsOfX[0].primeFactorExponent == 2;
    flagVerif = flagVerif && primeFactorsOfX[1].primeFactor == 5;
    flagVerif = flagVerif && primeFactorsOfX[1].primeFactorExponent == 3;
    return flagVerif;
}

bool primeFactorizationExample2(){
    unsigned long long int xInput = 50;
    array<primeFactorMap, 10000> primeFactorsOfX = primeFactorization(xInput);
    bool flagVerif = primeFactorsOfX[0].primeFactor == 2;
    flagVerif = flagVerif && primeFactorsOfX[0].primeFactorExponent == 1;
    flagVerif = flagVerif && primeFactorsOfX[1].primeFactor == 5;
    flagVerif = flagVerif && primeFactorsOfX[1].primeFactorExponent == 2;
    return flagVerif;
}

bool primeFactorizationExample3(){
    unsigned long long int xInput = 150;
    array<primeFactorMap, 10000> primeFactorsOfX = primeFactorization(xInput);
    bool flagVerif = primeFactorsOfX[0].primeFactor == 2;
    flagVerif = flagVerif && primeFactorsOfX[0].primeFactorExponent == 1;
    flagVerif = flagVerif && primeFactorsOfX[1].primeFactor == 3;
    flagVerif = flagVerif && primeFactorsOfX[1].primeFactorExponent == 1;
    flagVerif = flagVerif && primeFactorsOfX[2].primeFactor == 5;
    flagVerif = flagVerif && primeFactorsOfX[2].primeFactorExponent == 2;
    return flagVerif;
}

bool primeFactorizationExample4(){
    unsigned long long int xInput = 13195;
    array<primeFactorMap, 10000> primeFactorsOfX = primeFactorization(xInput);
    bool flagVerif = primeFactorsOfX[0].primeFactor == 5;
    flagVerif = flagVerif && primeFactorsOfX[0].primeFactorExponent == 1;
    flagVerif = flagVerif && primeFactorsOfX[1].primeFactor == 7;
    flagVerif = flagVerif && primeFactorsOfX[1].primeFactorExponent == 1;
    flagVerif = flagVerif && primeFactorsOfX[2].primeFactor == 13;
    flagVerif = flagVerif && primeFactorsOfX[2].primeFactorExponent == 1;
    flagVerif = flagVerif && primeFactorsOfX[3].primeFactor == 29;
    flagVerif = flagVerif && primeFactorsOfX[3].primeFactorExponent == 1;
    return flagVerif;
}

int main(){
    assert(primalityTestExample1());
    assert(primalityTestExample2());
    assert(primalityTestExample3());
    assert(primalityTestExample4());
    assert(primalityTestExample5());
    assert(primalityTestExample6());
    assert(primalityTestExample7());
    assert(!primalityTestExample8());
    assert(!primalityTestExample9());
    assert(!primalityTestExample10());
    assert(!primalityTestExample11());
    assert(!primalityTestExample12());
    assert(!primalityTestExample13());
    assert(!primalityTestExample14());
    assert(primeFactorizationExample1());
    assert(primeFactorizationExample2());
    assert(primeFactorizationExample3());
    assert(primeFactorizationExample4());
    
    unsigned long long int xInput = 600851475143;
    array<primeFactorMap, 10000> primeFactorsOfX = primeFactorizationScaledUp(xInput);
    int k = 0, kMax = 0;
    for(k = 0; k < 100; k++){
        if(primeFactorsOfX[k].primeFactor == 0){
            kMax = k;
            break;
        }
    }
    int kArgMax = 0;
    unsigned long long int maxPrimeFactor = primeFactorsOfX[kArgMax].primeFactor;
    for(k = 1; k <= kMax; k++){
        if(maxPrimeFactor < primeFactorsOfX[k].primeFactor){
            kArgMax = k;
            maxPrimeFactor = primeFactorsOfX[k].primeFactor;
        }
    }
    assert(maxPrimeFactor == 6857);
    return 0;
}