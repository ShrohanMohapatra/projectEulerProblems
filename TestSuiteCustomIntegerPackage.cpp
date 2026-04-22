// TestSuiteCustomIntegerPackage.cpp

#include"CustomIntegerPackage.h"
#include<cassert>
#include<iostream>
#include<cstdlib>

using namespace std;

void testCaseNumberFormationFromDigit(){
	struct linkedListNumber *newNumber;
	struct linkedListNumber *digitTracker;
	newNumber = new linkedListNumber;
	createNumberHolder(newNumber, 1);
	addDigitToNumber(&newNumber, 2);
	addDigitToNumber(&newNumber, 2);
	addDigitToNumber(&newNumber, 5);

	digitTracker = newNumber;

	assert(digitTracker->digit == 5);
	assert(digitTracker->digitPlace == 3);

	digitTracker = digitTracker->nextDigit;
	
	assert(digitTracker->digit == 2);
	assert(digitTracker->digitPlace == 2);
	
	digitTracker = digitTracker->nextDigit;

	assert(digitTracker->digit == 2);
	assert(digitTracker->digitPlace == 1);
	
	digitTracker = digitTracker->nextDigit;
	
	assert(digitTracker->digit == 1);
	assert(digitTracker->digitPlace == 0);
	
	digitTracker = digitTracker->nextDigit;
	
	assert(digitTracker == NULL);
}

void testCaseDigitalReverse(){
	struct linkedListNumber *numberPlaceHolder;
	struct linkedListNumber *digitalReversePlaceHolder;
	struct linkedListNumber *digitTracker;	
	// **************************************************************
	numberPlaceHolder = new linkedListNumber;
	createNumberHolder(numberPlaceHolder, 1);
	addDigitToNumber(&numberPlaceHolder, 2);
	addDigitToNumber(&numberPlaceHolder, 3);
	addDigitToNumber(&numberPlaceHolder, 4);
	addDigitToNumber(&numberPlaceHolder, 5);
	// **************************************************************
	digitalReversePlaceHolder = new linkedListNumber;
	createNumberHolder(digitalReversePlaceHolder, 1);
	addDigitToNumber(&digitalReversePlaceHolder, 2);
	addDigitToNumber(&digitalReversePlaceHolder, 3);
	addDigitToNumber(&digitalReversePlaceHolder, 4);
	addDigitToNumber(&digitalReversePlaceHolder, 5);
	// **************************************************************
	digitTracker = numberPlaceHolder;
	assert(digitTracker->digit == 5);
	assert(digitTracker->digitPlace == 4);
	// **************************************************************
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 4);
	assert(digitTracker->digitPlace == 3);
	// **************************************************************
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 3);
	assert(digitTracker->digitPlace == 2);
	// **************************************************************
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 2);
	assert(digitTracker->digitPlace == 1);
	// **************************************************************
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 1);
	assert(digitTracker->digitPlace == 0);
	// **************************************************************
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);
	// **************************************************************
	digitTracker = digitalReversePlaceHolder;
	assert(digitTracker->digit == 5);
	assert(digitTracker->digitPlace == 4);
	// **************************************************************
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 4);
	assert(digitTracker->digitPlace == 3);
	// **************************************************************
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 3);
	assert(digitTracker->digitPlace == 2);
	// **************************************************************
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 2);
	assert(digitTracker->digitPlace == 1);
	// **************************************************************
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 1);
	assert(digitTracker->digitPlace == 0);
	// **************************************************************
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);
	// **************************************************************
	numberDigitalReverse(&digitalReversePlaceHolder);
	// **************************************************************
	digitTracker = digitalReversePlaceHolder;
	assert(digitTracker->digit == 1);
	assert(digitTracker->digitPlace == 4);
	digitTracker = digitTracker->nextDigit;
	// **************************************************************
	assert(digitTracker->digit == 2);
	assert(digitTracker->digitPlace == 3);
	digitTracker = digitTracker->nextDigit;
	// **************************************************************
	assert(digitTracker->digit == 3);
	assert(digitTracker->digitPlace == 2);
	digitTracker = digitTracker->nextDigit;
	// **************************************************************
	assert(digitTracker->digit == 4);
	assert(digitTracker->digitPlace == 1);
	digitTracker = digitTracker->nextDigit;
	// **************************************************************
	assert(digitTracker->digit == 5);
	assert(digitTracker->digitPlace == 0);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);
	// **************************************************************
}


void testCaseRippleCarryAdderTwoNumberAdditionExample1(){
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *newNumber3;
	struct linkedListNumber *digitTracker;
	unsigned int carryDigit;

	newNumber1 = new linkedListNumber;
	createNumberHolder(newNumber1, 3);
	addDigitToNumber(&newNumber1, 4);
	addDigitToNumber(&newNumber1, 5);

	digitTracker = newNumber1;
	assert(digitTracker->digit == 5);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 4);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 3);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber2 = new linkedListNumber;
	createNumberHolder(newNumber2, 2);
	addDigitToNumber(&newNumber2, 1);
	addDigitToNumber(&newNumber2, 4);
	
	digitTracker = newNumber2;
	assert(digitTracker->digit == 4);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 2);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber3 = new linkedListNumber;

	rippleCarryAdder(newNumber1, newNumber2, &newNumber3, &carryDigit);
	digitTracker = newNumber3;
	assert(digitTracker->digit == 9);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 5);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 5);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == 	NULL);
}

void testCaseRippleCarryAdderTwoNumberAdditionExample2(){
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *newNumber3;
	struct linkedListNumber *digitTracker;
	unsigned int carryDigit;

	newNumber1 = new linkedListNumber;
	createNumberHolder(newNumber1, 4);
	addDigitToNumber(&newNumber1, 3);
	addDigitToNumber(&newNumber1, 5);
	addDigitToNumber(&newNumber1, 9);

	digitTracker = newNumber1;
	assert(digitTracker->digit == 9);
	assert(digitTracker->digitPlace == 3);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 5);
	assert(digitTracker->digitPlace == 2);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 3);
	assert(digitTracker->digitPlace == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 4);
	assert(digitTracker->digitPlace == 0);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber2 = new linkedListNumber;
	createNumberHolder(newNumber2, 7);
	addDigitToNumber(&newNumber2, 5);
	addDigitToNumber(&newNumber2, 1);
	addDigitToNumber(&newNumber2, 8);
	
	digitTracker = newNumber2;
	assert(digitTracker->digit == 8);
	assert(digitTracker->digitPlace == 3);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 1);
	assert(digitTracker->digitPlace == 2);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 5);
	assert(digitTracker->digitPlace == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 7);
	assert(digitTracker->digitPlace == 0);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber3 = new linkedListNumber;

	rippleCarryAdder(newNumber1, newNumber2, &newNumber3, &carryDigit);
	digitTracker = newNumber3;
	assert(digitTracker->digit == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 7);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 6);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 9);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == 	NULL);
}

void testCaseRippleCarryAdderTwoNumberAdditionExample3(){
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *newNumber3;
	struct linkedListNumber *digitTracker;
	unsigned int carryDigit;

	newNumber1 = new linkedListNumber;
	createNumberHolder(newNumber1, 7);

	digitTracker = newNumber1;
	assert(digitTracker->digit == 7);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber2 = new linkedListNumber;
	createNumberHolder(newNumber2, 7);
	
	digitTracker = newNumber2;
	assert(digitTracker->digit == 7);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber3 = new linkedListNumber;

	rippleCarryAdder(newNumber1, newNumber2, &newNumber3, &carryDigit);
	digitTracker = newNumber3;
	assert(digitTracker->digit == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 4);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == 	NULL);
}

void testCaseRippleCarryAdderTwoNumberAdditionExample4(){
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *newNumber3;
	struct linkedListNumber *digitTracker;
	unsigned int carryDigit;

	newNumber1 = new linkedListNumber;
	createNumberHolder(newNumber1, 7);
	addDigitToNumber(&newNumber1, 1);

	digitTracker = newNumber1;
	assert(digitTracker->digit == 1);
	assert(digitTracker->digitPlace == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 7);
	assert(digitTracker->digitPlace == 0);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber2 = new linkedListNumber;
	createNumberHolder(newNumber2, 7);
	
	digitTracker = newNumber2;
	assert(digitTracker->digit == 7);
	assert(digitTracker->digitPlace == 0);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber3 = new linkedListNumber;

	rippleCarryAdder(newNumber1, newNumber2, &newNumber3, &carryDigit);
	digitTracker = newNumber3;
	assert(digitTracker->digit == 2);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 4);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == 	NULL);
}

void testCaseCarryLookAheadAdderTwoNumberAdditionExample1(){
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *newNumber3;
	struct linkedListNumber *digitTracker;
	unsigned int carryDigit;

	newNumber1 = new linkedListNumber;
	createNumberHolder(newNumber1, 3);
	addDigitToNumber(&newNumber1, 4);
	addDigitToNumber(&newNumber1, 5);

	digitTracker = newNumber1;
	assert(digitTracker->digit == 5);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 4);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 3);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber2 = new linkedListNumber;
	createNumberHolder(newNumber2, 2);
	addDigitToNumber(&newNumber2, 1);
	addDigitToNumber(&newNumber2, 4);
	
	digitTracker = newNumber2;
	assert(digitTracker->digit == 4);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 2);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber3 = new linkedListNumber;

	carryLookAheadAdder(newNumber1, newNumber2, &newNumber3, &carryDigit);
	digitTracker = newNumber3;
	assert(digitTracker->digit == 9);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 5);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 5);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == 	NULL);
}

void testCaseCarryLookAheadAdderTwoNumberAdditionExample2(){
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *newNumber3;
	struct linkedListNumber *digitTracker;
	unsigned int carryDigit;

	newNumber1 = new linkedListNumber;
	createNumberHolder(newNumber1, 4);
	addDigitToNumber(&newNumber1, 3);
	addDigitToNumber(&newNumber1, 5);
	addDigitToNumber(&newNumber1, 9);

	digitTracker = newNumber1;
	assert(digitTracker->digit == 9);
	assert(digitTracker->digitPlace == 3);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 5);
	assert(digitTracker->digitPlace == 2);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 3);
	assert(digitTracker->digitPlace == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 4);
	assert(digitTracker->digitPlace == 0);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber2 = new linkedListNumber;
	createNumberHolder(newNumber2, 7);
	addDigitToNumber(&newNumber2, 5);
	addDigitToNumber(&newNumber2, 1);
	addDigitToNumber(&newNumber2, 8);
	
	digitTracker = newNumber2;
	assert(digitTracker->digit == 8);
	assert(digitTracker->digitPlace == 3);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 1);
	assert(digitTracker->digitPlace == 2);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 5);
	assert(digitTracker->digitPlace == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 7);
	assert(digitTracker->digitPlace == 0);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber3 = new linkedListNumber;

	carryLookAheadAdder(newNumber1, newNumber2, &newNumber3, &carryDigit);
	digitTracker = newNumber3;
	assert(digitTracker->digit == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 7);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 6);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 9);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == 	NULL);
}

void testCaseCarryLookAheadAdderTwoNumberAdditionExample3(){
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *newNumber3;
	struct linkedListNumber *digitTracker;
	unsigned int carryDigit;

	newNumber1 = new linkedListNumber;
	createNumberHolder(newNumber1, 7);

	digitTracker = newNumber1;
	assert(digitTracker->digit == 7);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber2 = new linkedListNumber;
	createNumberHolder(newNumber2, 7);
	
	digitTracker = newNumber2;
	assert(digitTracker->digit == 7);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber3 = new linkedListNumber;

	rippleCarryAdder(newNumber1, newNumber2, &newNumber3, &carryDigit);
	digitTracker = newNumber3;
	assert(digitTracker->digit == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 4);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == 	NULL);
}

void testCaseCarryLookAheadAdderTwoNumberAdditionExample4(){
	struct linkedListNumber *newNumber1;
	struct linkedListNumber *newNumber2;
	struct linkedListNumber *newNumber3;
	struct linkedListNumber *digitTracker;
	unsigned int carryDigit;

	newNumber1 = new linkedListNumber;
	createNumberHolder(newNumber1, 7);
	addDigitToNumber(&newNumber1, 1);

	digitTracker = newNumber1;
	assert(digitTracker->digit == 1);
	assert(digitTracker->digitPlace == 1);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 7);
	assert(digitTracker->digitPlace == 0);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber2 = new linkedListNumber;
	createNumberHolder(newNumber2, 7);
	
	digitTracker = newNumber2;
	assert(digitTracker->digit == 7);
	assert(digitTracker->digitPlace == 0);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == NULL);

	newNumber3 = new linkedListNumber;

	carryLookAheadAdder(newNumber1, newNumber2, &newNumber3, &carryDigit);
	digitTracker = newNumber3;
	assert(digitTracker->digit == 2);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker->digit == 4);
	digitTracker = digitTracker->nextDigit;
	assert(digitTracker == 	NULL);
}

int main(){
	testCaseNumberFormationFromDigit();
	testCaseDigitalReverse();
	testCaseRippleCarryAdderTwoNumberAdditionExample1();
	testCaseRippleCarryAdderTwoNumberAdditionExample2();
	testCaseRippleCarryAdderTwoNumberAdditionExample3();
	testCaseRippleCarryAdderTwoNumberAdditionExample4();
	testCaseCarryLookAheadAdderTwoNumberAdditionExample1();
	testCaseCarryLookAheadAdderTwoNumberAdditionExample2();
	testCaseCarryLookAheadAdderTwoNumberAdditionExample3();
	testCaseCarryLookAheadAdderTwoNumberAdditionExample4();
	return 0;
}
