// ProjectEulerProblem1.c

#include<iostream>
using namespace std;

int main(){
    unsigned long long int sumOfMultiples = 0;
    int i;
    for(i = 1; i < 1000; i++){
        if (i % 3 == 0 || i % 5 == 0){
            sumOfMultiples = sumOfMultiples + i;
        }
    }
    cout << "Sum of multiples of 3 or 5 = " << sumOfMultiples << endl;
    return 0;
}
