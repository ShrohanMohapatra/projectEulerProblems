// ProjectEulerProblem16.cpp

#include<iostream>
#include<cmath>
#include<cassert>
#include<array>

using namespace std;

array<unsigned long long int, 1000> powerOfTwoListGenerator(unsigned long long int powerMax){
    array<unsigned long long int, 1000> listOfPowerTwo;
    long long int k;
    unsigned long long int powerOfTwo = 1;
    for(k = 0; k <= static_cast<long long int>(powerMax); k = k + 1){
        listOfPowerTwo[k] = powerOfTwo;
        powerOfTwo = powerOfTwo * 2;
    }
    return listOfPowerTwo;
}

unsigned long long int numberOfDigits(unsigned long long int inputNumber){
    if(inputNumber == 0){
        return 0;
    }
    else{
        unsigned long long int bufferNumber = inputNumber;
        long long int digitCounter = 0;
        while (bufferNumber >= 1){
            digitCounter = digitCounter + 1;
            bufferNumber = bufferNumber / 10;
        }
        return digitCounter;
    }
}

array<unsigned long long int, 100> listOfDigits(unsigned long long int inputNumber){
    array<unsigned long long int, 100> targetList;
    unsigned long long int bufferNumber = inputNumber;
    unsigned long long int digitCount = numberOfDigits(inputNumber);
    long long int k;
    for(k = static_cast<long long int>(digitCount-1); k >= 0; k = k - 1){
        targetList[k] = bufferNumber % 10;
        bufferNumber = bufferNumber / 10;
        }
    return targetList;
}

array<unsigned long long int, 2000> powerOfTwoListGeneratorUpgraded(unsigned long long int powerMax){
    array<unsigned long long int, 2000> listOfPowerTwo;
    long long int k;
    unsigned long long int powerOfTwo = 1;
    for(k = 0; k <= static_cast<long long int>(powerMax); k = k + 1){
        listOfPowerTwo[k] = powerOfTwo;
        powerOfTwo = powerOfTwo * 2;
    }
    return listOfPowerTwo;
}

array<unsigned long long int, 500> listOfDigitsUpgraded(unsigned long long int inputNumber){
    array<unsigned long long int, 500> targetList;
    unsigned long long int bufferNumber = inputNumber;
    unsigned long long int digitCount = numberOfDigits(inputNumber);
    long long int k;
    for(k = static_cast<long long int>(digitCount-1); k >= 0; k = k - 1){
        targetList[k] = bufferNumber % 10;
        bufferNumber = bufferNumber / 10;
        }
    return targetList;
}

bool PowersOfTwoListGeneratorExample(){
    unsigned long long int maxPowerOfTwo = 16;
    array<unsigned long long int, 1000> listOfPowerTwo;
    listOfPowerTwo = powerOfTwoListGenerator(maxPowerOfTwo);
    bool flagVerif = listOfPowerTwo[0] == 1;
    flagVerif = flagVerif && listOfPowerTwo[1] == 2;
    flagVerif = flagVerif && listOfPowerTwo[2] == 4;
    flagVerif = flagVerif && listOfPowerTwo[3] == 8;
    flagVerif = flagVerif && listOfPowerTwo[4] == 16;
    flagVerif = flagVerif && listOfPowerTwo[5] == 32;
    flagVerif = flagVerif && listOfPowerTwo[6] == 64;
    flagVerif = flagVerif && listOfPowerTwo[7] == 128;
    flagVerif = flagVerif && listOfPowerTwo[8] == 256;
    flagVerif = flagVerif && listOfPowerTwo[9] == 512;
    flagVerif = flagVerif && listOfPowerTwo[10] == 1024;
    flagVerif = flagVerif && listOfPowerTwo[11] == 2048;
    flagVerif = flagVerif && listOfPowerTwo[12] == 4096;
    flagVerif = flagVerif && listOfPowerTwo[13] == 8192;
    flagVerif = flagVerif && listOfPowerTwo[14] == 16384;
    flagVerif = flagVerif && listOfPowerTwo[15] == 32768;
    flagVerif = flagVerif && listOfPowerTwo[16] == 65536;
    return flagVerif;
}

bool digitCountVerifExample1(){
    unsigned long long int inputNumber;
    unsigned long long int digitCounter;
    inputNumber = 1;
    digitCounter = numberOfDigits(inputNumber);
    return digitCounter == 1;
}

bool digitCountVerifExample2(){
    unsigned long long int inputNumber;
    unsigned long long int digitCounter;
    inputNumber = 10;
    digitCounter = numberOfDigits(inputNumber);
    return digitCounter == 2;
}

bool digitCountVerifExample3(){
    unsigned long long int inputNumber;
    unsigned long long int digitCounter;
    inputNumber = 100;
    digitCounter = numberOfDigits(inputNumber);
    return digitCounter == 3;
}

bool digitCountVerifExample4(){
    unsigned long long int inputNumber;
    unsigned long long int digitCounter;
    inputNumber = 1000;
    digitCounter = numberOfDigits(inputNumber);
    return digitCounter == 4;
}

bool digitCountVerifExample5(){
    unsigned long long int inputNumber;
    unsigned long long int digitCounter;
    inputNumber = 2;
    digitCounter = numberOfDigits(inputNumber);
    return digitCounter == 1;
}

bool digitCountVerifExample6(){
    unsigned long long int inputNumber;
    unsigned long long int digitCounter;
    inputNumber = 20;
    digitCounter = numberOfDigits(inputNumber);
    return digitCounter == 2;
}

bool digitCountVerifExample7(){
    unsigned long long int inputNumber;
    unsigned long long int digitCounter;
    inputNumber = 8327775461;
    digitCounter = numberOfDigits(inputNumber);
    return digitCounter == 10;
}

bool digitCountVerifExample8(){
    unsigned long long int inputNumber;
    unsigned long long int digitCounter;
    inputNumber = 8371;
    digitCounter = numberOfDigits(inputNumber);
    return digitCounter == 4;
}

bool listOfDigitsExample1(){
    array<unsigned long long int, 100> digitList;
    unsigned long long int testNumber = 100;
    digitList = listOfDigits(testNumber);
    bool flagVerif = digitList[0] == 1;
    flagVerif = flagVerif && digitList[1] == 0;
    flagVerif = flagVerif && digitList[2] == 0;
    return flagVerif;
}

bool listOfDigitsExample2(){
    array<unsigned long long int, 100> digitList;
    unsigned long long int testNumber = 1452;
    digitList = listOfDigits(testNumber);
    bool flagVerif = digitList[0] == 1;
    flagVerif = flagVerif && digitList[1] == 4;
    flagVerif = flagVerif && digitList[2] == 5;
    flagVerif = flagVerif && digitList[3] == 2;
    return flagVerif;
}

bool listOfDigitsBaseCaseExample(){
    array<unsigned long long int, 100> digitList;
    array<unsigned long long int, 1000> listOfPowersOfTwo;
    listOfPowersOfTwo = powerOfTwoListGenerator(20);
    unsigned long long int testNumber = listOfPowersOfTwo[15];
    digitList = listOfDigits(testNumber);
    bool flagVerif = digitList[0] == 3;
    flagVerif = flagVerif && digitList[1] == 2;
    flagVerif = flagVerif && digitList[2] == 7;
    flagVerif = flagVerif && digitList[3] == 6;
    flagVerif = flagVerif && digitList[4] == 8;
    return flagVerif;
}

void powerDigitSum(){
    array<unsigned long long int, 500> digitList;
    array<unsigned long long int, 2000> listOfPowersOfTwo;
    listOfPowersOfTwo = powerOfTwoListGeneratorUpgraded(1200);
    unsigned long long int testNumber = listOfPowersOfTwo[20];
    cout << "2^20 = " << testNumber << endl;
}

int main(){
    assert(PowersOfTwoListGeneratorExample());
    assert(digitCountVerifExample1());
    assert(digitCountVerifExample2());
    assert(digitCountVerifExample3());
    assert(digitCountVerifExample4());
    assert(digitCountVerifExample5());
    assert(digitCountVerifExample6());
    assert(digitCountVerifExample7());
    assert(digitCountVerifExample8());
    assert(listOfDigitsExample1());
    assert(listOfDigitsExample2());
    assert(listOfDigitsBaseCaseExample());
    // powerDigitSum();
    return 0;
}