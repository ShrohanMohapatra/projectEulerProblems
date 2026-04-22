// CustomIntegerPackage.h

#include<cassert>
#include<iostream>
#include<cstdlib>

using namespace std;

struct linkedListNumber{
	int digit;
	unsigned long long int digitPlace;
	linkedListNumber *nextDigit;
};

void createNumberHolder(struct linkedListNumber *numberHolder, int digitData){
	assert(0 <= digitData && digitData <= 9);
	numberHolder->digit = digitData;
	numberHolder->digitPlace = 0;
	numberHolder->nextDigit = NULL;
}

void addDigitToNumber(struct linkedListNumber **numberHolder, int digitData){
	assert(0 <= digitData && digitData <= 9);
	struct linkedListNumber* newDigitHolder;
	newDigitHolder = new linkedListNumber;
	newDigitHolder->digit = digitData;
	newDigitHolder->digitPlace = (*numberHolder)->digitPlace + 1;
	newDigitHolder->nextDigit = *numberHolder;
	*numberHolder = newDigitHolder;
}

void numberDigitalReverse(struct linkedListNumber **numberPlaceHolder){
	struct linkedListNumber *previousDigitTracker;
	struct linkedListNumber *currentDigitTracker;
	struct linkedListNumber *bufferPlaceHolder;
	bool flagFirstElementVisit = true;
	previousDigitTracker = (*numberPlaceHolder);
	currentDigitTracker = (*numberPlaceHolder);
	bufferPlaceHolder = new linkedListNumber;
	while(currentDigitTracker != NULL){
		if(flagFirstElementVisit){
			createNumberHolder(bufferPlaceHolder, currentDigitTracker->digit);
			flagFirstElementVisit = false;
		}
		else{
			addDigitToNumber(&bufferPlaceHolder, currentDigitTracker->digit);
		}
		previousDigitTracker = currentDigitTracker;
		currentDigitTracker = currentDigitTracker->nextDigit;
	}
	(*numberPlaceHolder) = bufferPlaceHolder;
}

void rippleCarryAdder(
		struct linkedListNumber *number1,
		struct linkedListNumber *number2,
		struct linkedListNumber **number3,
		unsigned int *carryDigit){
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *digitTrackerV1;
	struct linkedListNumber *digitTrackerV2;
	int digitTracker = 0;
	int flagMinNumber, sumDigit;
	unsigned long long int numberOfDigitsInNumber1 = number1->digitPlace+1;
	unsigned long long int numberOfDigitsInNumber2 = number2->digitPlace+1;
	
	newNumber1 = new linkedListNumber;
	digitTrackerV1 = number1;
	while(digitTrackerV1 != NULL){
		if(digitTracker == 0){
			createNumberHolder(newNumber1, digitTrackerV1->digit);
		}
		else{
			addDigitToNumber(&newNumber1, digitTrackerV1->digit);
		}
		digitTracker = digitTracker + 1;
		digitTrackerV1 = digitTrackerV1 -> nextDigit;
	}

	newNumber2 = new linkedListNumber;
	digitTracker = 0;
	digitTrackerV2 = number2;
	while(digitTrackerV2 != NULL){
		if(digitTracker == 0){
			createNumberHolder(newNumber2, digitTrackerV2->digit);
		}
		else{
			addDigitToNumber(&newNumber2, digitTrackerV2->digit);
		}
		digitTracker = digitTracker + 1;
		digitTrackerV2 = digitTrackerV2->nextDigit;
	}

	unsigned long long int minNumberOfDigits;
	if(numberOfDigitsInNumber1 < numberOfDigitsInNumber2){
		minNumberOfDigits = numberOfDigitsInNumber1;
		flagMinNumber = 1;
	}
	else{
		minNumberOfDigits = numberOfDigitsInNumber2;
		flagMinNumber = 2;
	}
	int intFunctionCarryDigit = 0;
	int digit1, digit2, bufferDigit;
	digitTracker = 0;
	digitTrackerV1 = newNumber1;
	digitTrackerV2 = newNumber2;

	struct linkedListNumber *newNumber3;
	newNumber3 = new linkedListNumber;
	while(digitTracker < minNumberOfDigits && digitTrackerV1 != NULL && digitTrackerV2 != NULL){
		digit1 = digitTrackerV1->digit;
		digit2 = digitTrackerV2->digit;
		sumDigit = (digit1 + digit2 + intFunctionCarryDigit) % 10;
		intFunctionCarryDigit = (digit1 + digit2 + intFunctionCarryDigit) / 10;
		if(digitTracker == 0){
			createNumberHolder(newNumber3, sumDigit);
		}
		else{
			addDigitToNumber(&newNumber3, sumDigit);
		}
		digitTrackerV1 = digitTrackerV1->nextDigit;
		digitTrackerV2 = digitTrackerV2->nextDigit;
		digitTracker = digitTracker + 1;
	}
	if(flagMinNumber == 1){
		while(digitTrackerV2 != NULL){
			bufferDigit = digitTrackerV2->digit;
			sumDigit = (bufferDigit + intFunctionCarryDigit) % 10;
			intFunctionCarryDigit = (bufferDigit + intFunctionCarryDigit) / 10;
			addDigitToNumber(&newNumber3, sumDigit);
			digitTrackerV2 = digitTrackerV2->nextDigit;
		}
	}
	else{
		while(digitTrackerV1 != NULL){
			bufferDigit = digitTrackerV1->digit;
			sumDigit = (bufferDigit + intFunctionCarryDigit) % 10;
			intFunctionCarryDigit = (bufferDigit + intFunctionCarryDigit) / 10;
			addDigitToNumber(&newNumber3, sumDigit);
			digitTrackerV1 = digitTrackerV1->nextDigit;
		}
	}
	if(intFunctionCarryDigit != 0){
		addDigitToNumber(&newNumber3, intFunctionCarryDigit);
	}
	*(number3) = newNumber3;
	*(carryDigit) = intFunctionCarryDigit;
}

void carryLookAheadAdder(
		struct linkedListNumber *number1,
		struct linkedListNumber *number2,
		struct linkedListNumber **number3,
		unsigned int *carryDigit){
	int lookAheadSum[10][10][10], lookAheadCarry[10][10][10], k1, k2, k3;
	for(k1 = 0; k1 < 10; k1++){
		for(k2 = 0; k2 < 10; k2++){
			for(k3 = 0; k3 < 10; k3++){
				lookAheadSum[k1][k2][k3] = (k1 + k2 + k3) % 10;
				lookAheadCarry[k1][k2][k3] = (k1 + k2 + k3) / 10;
			}
		}
	}
	int twoDimLookAheadSum[10][10], twoDimLookAheadCarry[10][10];
	for(k1 = 0; k1 < 10; k1++){
		for(k2 = 0; k2 < 10; k2++){
			twoDimLookAheadSum[k1][k2] = (k1 + k2) % 10;
			twoDimLookAheadCarry[k1][k2] = (k1 + k2) / 10;
		}
	}
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *digitTrackerV1;
	struct linkedListNumber *digitTrackerV2;
	int digitTracker = 0;
	int flagMinNumber, sumDigit;
	unsigned long long int numberOfDigitsInNumber1 = number1->digitPlace+1;
	unsigned long long int numberOfDigitsInNumber2 = number2->digitPlace+1;
	
	newNumber1 = new linkedListNumber;
	digitTrackerV1 = number1;
	while(digitTrackerV1 != NULL){
		if(digitTracker == 0){
			createNumberHolder(newNumber1, digitTrackerV1->digit);
		}
		else{
			addDigitToNumber(&newNumber1, digitTrackerV1->digit);
		}
		digitTracker = digitTracker + 1;
		digitTrackerV1 = digitTrackerV1 -> nextDigit;
	}

	newNumber2 = new linkedListNumber;
	digitTracker = 0;
	digitTrackerV2 = number2;
	while(digitTrackerV2 != NULL){
		if(digitTracker == 0){
			createNumberHolder(newNumber2, digitTrackerV2->digit);
		}
		else{
			addDigitToNumber(&newNumber2, digitTrackerV2->digit);
		}
		digitTracker = digitTracker + 1;
		digitTrackerV2 = digitTrackerV2->nextDigit;
	}

	unsigned long long int minNumberOfDigits;
	if(numberOfDigitsInNumber1 < numberOfDigitsInNumber2){
		minNumberOfDigits = numberOfDigitsInNumber1;
		flagMinNumber = 1;
	}
	else{
		minNumberOfDigits = numberOfDigitsInNumber2;
		flagMinNumber = 2;
	}
	int intFunctionCarryDigit = 0;
	int digit1, digit2, bufferDigit;
	digitTracker = 0;
	digitTrackerV1 = newNumber1;
	digitTrackerV2 = newNumber2;

	struct linkedListNumber *newNumber3;
	newNumber3 = new linkedListNumber;
	while(digitTracker < minNumberOfDigits && digitTrackerV1 != NULL && digitTrackerV2 != NULL){
		digit1 = digitTrackerV1->digit;
		digit2 = digitTrackerV2->digit;
		sumDigit = lookAheadSum[digit1][digit2][intFunctionCarryDigit];
		intFunctionCarryDigit = lookAheadCarry[digit1][digit2][intFunctionCarryDigit];
		if(digitTracker == 0){
			createNumberHolder(newNumber3, sumDigit);
		}
		else{
			addDigitToNumber(&newNumber3, sumDigit);
		}
		digitTrackerV1 = digitTrackerV1->nextDigit;
		digitTrackerV2 = digitTrackerV2->nextDigit;
		digitTracker = digitTracker + 1;
	}
	if(flagMinNumber == 1){
		while(digitTrackerV2 != NULL){
			bufferDigit = digitTrackerV2->digit;
			sumDigit = twoDimLookAheadSum[bufferDigit][intFunctionCarryDigit];
			intFunctionCarryDigit = twoDimLookAheadCarry[bufferDigit][intFunctionCarryDigit];
			addDigitToNumber(&newNumber3, sumDigit);
			digitTrackerV2 = digitTrackerV2->nextDigit;
		}
	}
	else{
		while(digitTrackerV1 != NULL){
			bufferDigit = digitTrackerV1->digit;
			sumDigit = twoDimLookAheadSum[bufferDigit][intFunctionCarryDigit];
			intFunctionCarryDigit = twoDimLookAheadCarry[bufferDigit][intFunctionCarryDigit];
			addDigitToNumber(&newNumber3, sumDigit);
			digitTrackerV1 = digitTrackerV1->nextDigit;
		}
	}
	if(intFunctionCarryDigit != 0){
		addDigitToNumber(&newNumber3, intFunctionCarryDigit);
	}
	*(number3) = newNumber3;
	*(carryDigit) = intFunctionCarryDigit;
}

void carryLookAheadSubtractor(
		struct linkedListNumber *number1,
		struct linkedListNumber *number2,
		struct linkedListNumber **number3,
		unsigned int *borrowDigit,
		int *plusMinusFlag){
	int lookAheadDiff[10][10][2], lookAheadBorrow[10][10][2], k1, k2;
	for(k1 = 0; k1 < 10; k1++){
		for(k2 = 0; k2 < 10; k2++){
			if(k1 >= k2){
				lookAheadDiff[k1][k2][0] = (k1 - k2) % 10;
				lookAheadBorrow[k1][k2][0] = 0;
				if(k1 >= k2 + 1){
					lookAheadDiff[k1][k2][1] = (k1 - k2 - 1) % 10;
					lookAheadBorrow[k1][k2][1] = 0;
				}
				else{
					lookAheadDiff[k1][k2][1] = (10 + k1 - k2 - 1) % 10;
					lookAheadBorrow[k1][k2][1] = 1;
				}
			}
			else{
				lookAheadDiff[k1][k2][0] = (10 + k1 - k2) % 10;
				lookAheadBorrow[k1][k2][0] = 1;
				if(10 + k1 - k2 - 1 >= 0){
					lookAheadDiff[k1][k2][1] = (10 + k1 - k2 - 1) % 10;
					lookAheadBorrow[k1][k2][1] = 0;
				}
			}
		}
	}
	int twoDimLookAheadDiff[10][2], twoDimLookAheadBorrow[10][2];
	twoDimLookAheadDiff[0][0] = 0;
	twoDimLookAheadBorrow[0][0] = 0;
	twoDimLookAheadDiff[0][1] = 9;
	twoDimLookAheadBorrow[0][1] = 1;
	for(k1 = 1; k1 < 10; k1++){
		twoDimLookAheadDiff[k1][0] = k1;
		twoDimLookAheadBorrow[k1][0] = 0;
		twoDimLookAheadDiff[k1][1] = k1-1;
		twoDimLookAheadBorrow[k1][1] = 0;
	}
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *digitTrackerV1;
	struct linkedListNumber *digitTrackerV2;
	int digitTracker = 0;
	int flagMinNumber, diffDigit;
	unsigned long long int numberOfDigitsInNumber1 = number1->digitPlace+1;
	unsigned long long int numberOfDigitsInNumber2 = number2->digitPlace+1;
	
	newNumber1 = new linkedListNumber;
	digitTrackerV1 = number1;
	while(digitTrackerV1 != NULL){
		if(digitTracker == 0){
			createNumberHolder(newNumber1, digitTrackerV1->digit);
		}
		else{
			addDigitToNumber(&newNumber1, digitTrackerV1->digit);
		}
		digitTracker = digitTracker + 1;
		digitTrackerV1 = digitTrackerV1 -> nextDigit;
	}

	newNumber2 = new linkedListNumber;
	digitTracker = 0;
	digitTrackerV2 = number2;
	while(digitTrackerV2 != NULL){
		if(digitTracker == 0){
			createNumberHolder(newNumber2, digitTrackerV2->digit);
		}
		else{
			addDigitToNumber(&newNumber2, digitTrackerV2->digit);
		}
		digitTracker = digitTracker + 1;
		digitTrackerV2 = digitTrackerV2->nextDigit;
	}

	unsigned long long int minNumberOfDigits;
	if(numberOfDigitsInNumber1 < numberOfDigitsInNumber2){
		minNumberOfDigits = numberOfDigitsInNumber1;
		flagMinNumber = 1;
	}
	else{
		minNumberOfDigits = numberOfDigitsInNumber2;
		flagMinNumber = 2;
	}
	int intFunctionBorrowDigit = 0;
	int digit1, digit2, bufferDigit;
	digitTracker = 0;
	digitTrackerV1 = newNumber1;
	digitTrackerV2 = newNumber2;

	struct linkedListNumber *newNumber3;
	newNumber3 = new linkedListNumber;
	while(digitTracker < minNumberOfDigits && digitTrackerV1 != NULL && digitTrackerV2 != NULL){
		digit1 = digitTrackerV1->digit;
		digit2 = digitTrackerV2->digit;
		diffDigit = lookAheadDiff[digit1][digit2][intFunctionBorrowDigit];
		intFunctionBorrowDigit = lookAheadBorrow[digit1][digit2][intFunctionBorrowDigit];
		if(digitTracker == 0){
			createNumberHolder(newNumber3, diffDigit);
		}
		else{
			addDigitToNumber(&newNumber3, diffDigit);
		}
		digitTrackerV1 = digitTrackerV1->nextDigit;
		digitTrackerV2 = digitTrackerV2->nextDigit;
		digitTracker = digitTracker + 1;
	}
	if(flagMinNumber == 1){
		while(digitTrackerV2 != NULL){
			bufferDigit = digitTrackerV2->digit;
			diffDigit = twoDimLookAheadDiff[bufferDigit][intFunctionBorrowDigit];
			intFunctionBorrowDigit = twoDimLookAheadBorrow[bufferDigit][intFunctionBorrowDigit];
			addDigitToNumber(&newNumber3, diffDigit);
			digitTrackerV2 = digitTrackerV2->nextDigit;
		}
	}
	else{
		while(digitTrackerV1 != NULL){
			bufferDigit = digitTrackerV1->digit;
			diffDigit = twoDimLookAheadDiff[bufferDigit][intFunctionBorrowDigit];
			intFunctionBorrowDigit = twoDimLookAheadBorrow[bufferDigit][intFunctionBorrowDigit];
			addDigitToNumber(&newNumber3, diffDigit);
			digitTrackerV1 = digitTrackerV1->nextDigit;
		}
	}
	if(intFunctionBorrowDigit != 0){
		addDigitToNumber(&newNumber3, intFunctionBorrowDigit);
	}
	*(number3) = newNumber3;
	*(borrowDigit) = intFunctionBorrowDigit;
}

