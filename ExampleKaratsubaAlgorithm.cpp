// ExampleKaratsubaAlgorithm.cpp

#include<cassert>
#include<random>
#include<cmath>
// #include<iostream>

using namespace std;

/*
	The following are the set of functions intended for the future testing and rigorous utilization.
*/

unsigned int numberOfDigits(unsigned int n){
	if(n == 0){
		return 1;
	}
	else{
		unsigned int digitCount = 0;
		unsigned int bufferForN = n;
		while(bufferForN >= 1){
			digitCount ++;
			bufferForN /= 10;
		}
		return digitCount;
	}
}

void listOfDigits(unsigned int n, unsigned int digitList[15]){
	unsigned int digitCount = numberOfDigits(n);
	unsigned int k;
	unsigned int bufferForN = n;
	for(k = digitCount-1; k >= 0; k--){
		digitList[k] = bufferForN % 10;
		bufferForN /= 10;
	}
}

unsigned int karatsubaProduct(unsigned int n1, unsigned int n2){
	if(0 <= n1 && n1 <= 9 && 0 <= n2 && n2 <= 9){
		return n1*n2;
	}
	else{
		unsigned int digitCountN1, digitCountN2;
		unsigned int m, M, powerOfTenM;
		digitCountN1 = numberOfDigits(n1);
		digitCountN2 = numberOfDigits(n2);
		if(digitCountN1 >= digitCountN2){
			M = digitCountN1;
		}
		else{
			M = digitCountN2;
		}
		if(M % 2 == 1){
			M = M + 1;
		}
		powerOfTenM = 1;
		for(m = 1; m <= M; m++){
			powerOfTenM *= 10;
		}
		unsigned int x0, x1, y0, y1, z0, z1, z2, z3, z;
		x1 = n1 / powerOfTenM;
		x0 = n1 % powerOfTenM;
		y1 = n2 / powerOfTenM;
		y0 = n2 % powerOfTenM;
		z0 = karatsubaProduct(x0, y0);
		z2 = karatsubaProduct(x1, y1);
		z3 = karatsubaProduct(x1+x0, y1+y0);
		z1 = z3 - z0 - z2;
		z = powerOfTenM*(powerOfTenM*z2 + z1) + z0;
		return z;
	}
}

int ToomCookProduct(int n1, int n2){
	/*
		Toom-Cook actual implementation accelerates the digitwise multiplication
		of two positive integers:
		(1) Splitting
		(2) Evaluation
		(3) Pointwise multiplication
		(4) Interpolation
		(5) Recomposition

		// In the following example, I will directly borrow Wikipedia's test case
		// m = 12	3456	7890	1234	5678	9012
		// n = 9	8765	4321	9876	5432	1098

		
	*/
	return 1; // I will continue tomorrow
}

/*
	The following is the suite of test functions defined above and tested in the main() function.
*/

void digitCountTestCaseExample1(){
	assert(numberOfDigits(0) == 1);
}
void digitCountTestCaseExample2(){
	assert(numberOfDigits(1) == 1);
}
void digitCountTestCaseExample3(){
	unsigned int k;
	for(k = 2; k < 10; k++){
		assert(numberOfDigits(k) == 1);
	}
}
void digitCountTestCaseExample4(){
	unsigned int k;
	for(k = 10; k < 100; k++){
		assert(numberOfDigits(k) == 2);
	}
}
void digitCountTestCaseExample5(){
	unsigned int k;
	for(k = 100; k < 1000; k++){
		assert(numberOfDigits(k) == 3);
	}
}
void digitCountTestCaseExample6(){
	unsigned int k;
	for(k = 1000; k < 10000; k++){
		assert(numberOfDigits(k) == 4);
	}
}
void digitListTestCaseExample1(){
	unsigned int digitList[15];
	listOfDigits(1, digitList);
	assert(digitList[0] == 1);
}
void digitListTestCaseExample2(){
	unsigned int digitList[15];
	listOfDigits(1123, digitList);
	assert(digitList[0] == 1);
	assert(digitList[1] == 1);
	assert(digitList[2] == 2);
	assert(digitList[3] == 3);
}
void digitListTestCaseExample3(){
	unsigned int digitList[15];
	listOfDigits(200, digitList);
	assert(digitList[0] == 2);
	assert(digitList[1] == 0);
	assert(digitList[2] == 0);
}
void digitListTestCaseExample4(){
	unsigned int digitList[15];
	listOfDigits(10000, digitList);
	assert(digitList[0] == 1);
	assert(digitList[1] == 0);
	assert(digitList[2] == 0);
	assert(digitList[3] == 0);
	assert(digitList[4] == 0);
}
void karatsubaProductCheckExample1(){
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> distrib(10, 5000000);
	unsigned int x, y, z1, z2;
	x = distrib(gen);
	y = distrib(gen);
	z1 = karatsubaProduct(x, y);
	z2 = x*y;
	assert(z1 == z2);
}
void karatsubaProductCheckExample2(){
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> distrib(10, 5000000);
	unsigned int x, y, z1, z2;
	x = distrib(gen);
	y = distrib(gen);
	z1 = karatsubaProduct(x, y);
	z2 = x*y;
	assert(z1 == z2);
}
void karatsubaProductCheckExample3(){
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> distrib(10, 5000000);
	unsigned int x, y, z1, z2;
	x = distrib(gen);
	y = distrib(gen);
	z1 = karatsubaProduct(x, y);
	z2 = x*y;
	assert(z1 == z2);
}
void karatsubaProductCheckExample4(){
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> distrib(10, 5000000);
	unsigned int x, y, z1, z2;
	x = distrib(gen);
	y = distrib(gen);
	z1 = karatsubaProduct(x, y);
	z2 = x*y;
	assert(z1 == z2);
}
void karatsubaProductCheckExample5(){
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> distrib(10, 5000000);
	unsigned int x, y, z1, z2;
	x = distrib(gen);
	y = distrib(gen);
	z1 = karatsubaProduct(x, y);
	z2 = x*y;
	assert(z1 == z2);
}

// The main() function runs all these tests.

int main(){
	digitCountTestCaseExample1();
	digitCountTestCaseExample2();
	digitCountTestCaseExample3();
	digitCountTestCaseExample4();
	digitCountTestCaseExample5();
	digitCountTestCaseExample6();
	digitListTestCaseExample1();
	digitListTestCaseExample2();
	digitListTestCaseExample3();
	digitListTestCaseExample4();
	karatsubaProductCheckExample1();
	karatsubaProductCheckExample2();
	karatsubaProductCheckExample3();
	karatsubaProductCheckExample4();
	karatsubaProductCheckExample5();
	return 0;
}