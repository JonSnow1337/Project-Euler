/*  Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

*/

#include <iostream>

using namespace std;


bool isPrime(int number){
    bool numberIsPrime = true;

    for(int i=2;i<number;i++){
        if(number%i == 0){
            numberIsPrime = false;
            break;
        }
    }
    return numberIsPrime;
}


int main()
{
    int primeCount = 0;
    int _1001primeNumber;           // this will be the solution

    for(int i = 2;i<=1000000;i++){
        if(isPrime(i)){
            primeCount++;
            if(primeCount == 10001){
                cout<<i<<endl;
            }
        }
    }

    //cout<<difference<<endl;     // display the result
    return 0;
}
