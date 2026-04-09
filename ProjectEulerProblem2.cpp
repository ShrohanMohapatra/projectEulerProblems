// ProjectEulerProblem2.cpp

#include<array>
#include<cmath>
#include<cassert>

using namespace std;

array<unsigned long long int, 200>fibList (unsigned long long int numOfElems){
    array<unsigned long long int, 200> targetList;
    unsigned long int k;
    targetList[0] = 1;
    targetList[1] = 2;
    for(k = 2; k < numOfElems; k++){
        targetList[k] = targetList[k-1] + targetList[k-2];
    }
    return targetList;
}

unsigned long long int fibSeqTerm(unsigned long long int n){
    long double A = (5 + 3*sqrt(5))/10;
    long double B = (5 - 3*sqrt(5))/10;
    long double phi = (1 + sqrt(5))/2;
    long double psi = (1 - sqrt(5))/2;
    long double nIndex = static_cast<long double>(n);
    return static_cast<unsigned long long int>(A*pow(phi, nIndex) + B*pow(psi, nIndex));
}

bool fibonacciSequenceCheck(unsigned long long int nMax){
    array<unsigned long long int, 200> refFibSeq = fibList(nMax);
    array<unsigned long long int, 200> newRefFibSeq;
    for(long int k = 0; k < static_cast<long int>(nMax); k++){
        newRefFibSeq[k] = fibSeqTerm(static_cast<unsigned long long int>(k));
    }
    bool flagCheck = true;
    for(long int k = 0; k < static_cast<long int>(nMax); k++){
        flagCheck = flagCheck && fabs(refFibSeq[k] - newRefFibSeq[k]) < pow(10.0000, -16.000);
    }
    return flagCheck;
}

bool mainFunctionDriver(){
    unsigned long long int nMax = 101;
    array<unsigned long long int, 200> newRefFibSeq;
    for(long int k = 0; k < static_cast<long int>(nMax); k++){
        newRefFibSeq[k] = fibSeqTerm(static_cast<unsigned long long int>(k));
    }
    int k, kIndexMax;
    for(k = 1; k < static_cast<int>(nMax); k++){
        if(newRefFibSeq[k] > 4000000){
            kIndexMax = k;
            break;
        }
    }
    assert(newRefFibSeq[kIndexMax-1] <= 4000000);
    assert(kIndexMax == 32);
    long long int sumOfEvenValuedTerms = 0;
    for(k = 0; k < static_cast<int>(kIndexMax); k++){
        if(newRefFibSeq[k] % 2 == 0){
            sumOfEvenValuedTerms += static_cast<long long int>(newRefFibSeq[k]);
        }
    }
    assert(sumOfEvenValuedTerms == 4613732);
    return true;
}

int main(){
    unsigned long long int kMax = 70;
    assert(fibonacciSequenceCheck(kMax));
    assert(mainFunctionDriver());
    return 0;
}
