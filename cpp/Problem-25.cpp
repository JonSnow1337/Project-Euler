/*  Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

*/


/**** This solution is unoptimized, it takes over a minute to calculate****/

#include <iostream>
#include <vector>
#include "libs/BigInteger/BigIntegerSingleFile.cpp"

using namespace std;

int digitCount(BigInteger number){
    int length = 1;
    while ( number / 10 != 0 ){
        length++;
        number /= 10;
    }
   return length;
}

int main()
{
    vector<BigInteger> *_sequence = new vector<BigInteger>();
    _sequence->push_back(0);
    _sequence->push_back(1);
    _sequence->push_back(1);

    int digitcount;


    do{
        BigInteger lastNum((*_sequence)[_sequence->size() - 1]);
        BigInteger numBeforeLastNum((*_sequence)[_sequence->size() - 2]);
        BigInteger newNum = lastNum + numBeforeLastNum;
        digitcount = digitCount(newNum);
        _sequence->push_back(newNum);

        if(digitcount >= 1000){
            break;
        }

    }while(true);


    cout<<_sequence->size() - 1<<endl;

    return 0;
}
