// ProjectEulerProblem6.cpp

#include<iostream>
#include<cassert>
#include<cmath>
#include<array>

using namespace std;

unsigned long long int sumOfSquares(unsigned long long int n){
    return n*(n+1)*(2*n+1)/6;
}

unsigned long long int squareSumOfDifference(unsigned long long int n){
    return n*(n+1)*(3*n*n-n-2)/12;
}

bool boolSumOfSquaresV1(){
    unsigned long long int nMax = 10, k;
    unsigned long long int verifSum = 0, targetSum;
    for(k = 1; k <= nMax; k++){
        verifSum = verifSum + k*k;
    }
    targetSum = sumOfSquares(nMax);
    return verifSum == targetSum;
}

bool boolSumOfSquaresV2(){
    unsigned long long int nMax = 20, k;
    unsigned long long int verifSum = 0, targetSum;
    for(k = 1; k <= nMax; k++){
        verifSum = verifSum + k*k;
    }
    targetSum = sumOfSquares(nMax);
    return verifSum == targetSum;
}

bool boolSumOfSquaresV3(){
    unsigned long long int nMax = 30, k;
    unsigned long long int verifSum = 0, targetSum;
    for(k = 1; k <= nMax; k++){
        verifSum = verifSum + k*k;
    }
    targetSum = sumOfSquares(nMax);
    return verifSum == targetSum;
}

bool boolSumOfSquaresV4(){
    unsigned long long int nMax = 40, k;
    unsigned long long int verifSum = 0, targetSum;
    for(k = 1; k <= nMax; k++){
        verifSum = verifSum + k*k;
    }
    targetSum = sumOfSquares(nMax);
    return verifSum == targetSum;
}

bool boolSumOfSquaresV5(){
    unsigned long long int nMax = 100, k;
    unsigned long long int verifSum = 0, targetSum;
    for(k = 1; k <= nMax; k++){
        verifSum = verifSum + k*k;
    }
    targetSum = sumOfSquares(nMax);
    return verifSum == targetSum;
}

bool boolSumOfSquaresV6(){
    unsigned long long int nMax = 500, k;
    unsigned long long int verifSum = 0, targetSum;
    for(k = 1; k <= nMax; k++){
        verifSum = verifSum + k*k;
    }
    targetSum = sumOfSquares(nMax);
    return verifSum == targetSum;
}

bool boolSumOfSquaresV7(){
    unsigned long long int nMax = 7500, k;
    unsigned long long int verifSum = 0, targetSum;
    for(k = 1; k <= nMax; k++){
        verifSum = verifSum + k*k;
    }
    targetSum = sumOfSquares(nMax);
    return verifSum == targetSum;
}

bool SumSquareDifferenceVerifExampleV1(){
    unsigned long long int nMax = 10;
    unsigned long long int index;
    unsigned long long int sumOfSquares = 0;
    unsigned long long int squareOfSumOfNconsec = 0;
    unsigned long long int targetSumSquareDiff;
    unsigned long long int verifSumSquareDiff;
    for(index = 1; index <= nMax; index++){
        sumOfSquares = sumOfSquares + index*index;
        squareOfSumOfNconsec = squareOfSumOfNconsec + index;
    }
    squareOfSumOfNconsec = squareOfSumOfNconsec*squareOfSumOfNconsec;
    targetSumSquareDiff = squareOfSumOfNconsec - sumOfSquares;
    verifSumSquareDiff = squareSumOfDifference(nMax);
    assert(targetSumSquareDiff == verifSumSquareDiff);
    assert(targetSumSquareDiff == 2640);
}

bool SumSquareDifferenceVerifExampleV2(){
    unsigned long long int nMax = 100;
    unsigned long long int index;
    unsigned long long int sumOfSquares = 0;
    unsigned long long int squareOfSumOfNconsec = 0;
    unsigned long long int targetSumSquareDiff;
    unsigned long long int verifSumSquareDiff;
    for(index = 1; index <= nMax; index++){
        sumOfSquares = sumOfSquares + index*index;
        squareOfSumOfNconsec = squareOfSumOfNconsec + index;
    }
    squareOfSumOfNconsec = squareOfSumOfNconsec*squareOfSumOfNconsec;
    targetSumSquareDiff = squareOfSumOfNconsec - sumOfSquares;
    verifSumSquareDiff = squareSumOfDifference(nMax);
    assert(targetSumSquareDiff == verifSumSquareDiff);
    assert(targetSumSquareDiff == 25164150);
}

int main(){
    boolSumOfSquaresV1();
    boolSumOfSquaresV2();
    boolSumOfSquaresV3();
    boolSumOfSquaresV4();
    boolSumOfSquaresV5();
    boolSumOfSquaresV6();
    boolSumOfSquaresV7();
    SumSquareDifferenceVerifExampleV1();
    SumSquareDifferenceVerifExampleV2();
    return 0;
}