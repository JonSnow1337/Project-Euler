/*  Problem 16

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?

*/


/*
    For this problem we're using a big integer library by panks
    https://github.com/panks/BigInteger

    only BigIntegerSingleFile.cpp is required
*/

#include <iostream>
#include "libs/BigInteger/BigIntegerSingleFile.cpp"

using namespace std;

int main()
{
    const int base = 2;
    const int exponent = 1000;
    BigInteger _result("1");
    unsigned int _sum = 0;      // this is going to be the result


    for(int i=0;i<1000;i++){
        _result *= base;
    }

    // convert the number to a string (so we can split it later)
    string numberStr = _result.getNumber();

    for(int i=0;i<numberStr.size();i++){
        int n = (int)numberStr[i] - 48;     // convert char to int (-48 is needed because of ASCII conversion)
        _sum += n;
    }


    cout<<_sum<<endl;       // display the result
    return 0;
}
