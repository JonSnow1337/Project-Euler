/*  Problem 20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

*/




//     For this problem we're using a big integer library by panks
//     https://github.com/panks/BigInteger


#include <iostream>
#include <string>
#include "libs/BigInteger/BigIntegerSingleFile.cpp"

using namespace std;


int main()
{
    unsigned int num = 100;
    BigInteger factorielSum(1);
    BigInteger _sum = 0;                      // this will be the result



    while(num>0){
        factorielSum *= num;
        num--;
    }


    // split the sum into digits
    while(factorielSum>0)
    {
        BigInteger digit = factorielSum % 10;
        factorielSum = factorielSum / 10;
        _sum += digit;
    }

    cout<<_sum.getNumber()<<endl;           // display the solution
    return 0;
}
