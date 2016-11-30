/*  Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

*/




#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

unsigned long long int powerSum(unsigned long long int number){
    unsigned long long int _sum = 0;

    while (number > 0)
    {
        int digit = number%10;
        number /= 10;
        _sum += (unsigned long long int)pow(digit, 5);
    }

    return _sum;
}

int main()
{
    unsigned long long int _sum = 0;

    for(unsigned int i=2;i<1000000;i++){
        if(powerSum(i) == i){
            _sum += powerSum(i);
        }
    }


    cout<<_sum<<endl;
    return 0;
}
