/*  Problem 29

Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    2^2=4, 2^3=8, 2^4=16, 2^5=32
    3^2=9, 3^3=27, 3^4=81, 3^5=243
    4^2=16, 4^3=64, 4^4=256, 4^5=1024
    5^2=25, 5^3=125, 5^4=625, 5^5=3125

If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?


*/




#include <iostream>
#include <vector>
#include <algorithm>                                    // required for std sort function
#include <math.h>                                       // required for pow function
#include "libs/BigInteger/BigIntegerSingleFile.cpp"     // library to handle big numbers

using namespace std;


bool sortBySize(BigInteger a, BigInteger b){            // helper function for sort
    return a<b;
}


BigInteger _power( BigInteger val, BigInteger _pow ) {
	if ( _pow <= 0 )
		return 1;
	return val * _power( val, _pow -1 );
}


int main()
{
    unsigned int _termCount = 0;                // number of distinct items, this will  be the solution
    vector<BigInteger> numbers;

    const unsigned long long int minimum = 2;                      // constants
    const unsigned long long int maximum = 100;


    for(unsigned long long int i=2;i<=maximum;i++){
        for(unsigned long long int j=2;j<=maximum;j++){
            //cout<<(int)pow(i,j)<<endl;
            BigInteger number(0);
            number = _power(i,j);
            numbers.push_back(number);

        }
    }

    sort(numbers.begin(), numbers.end(), sortBySize);                           // sort by size
    numbers.erase( unique( numbers.begin(), numbers.end() ), numbers.end());    // remove duplicates
    _termCount = numbers.size();

    cout<<_termCount<<endl;                                                     // display the solution
    return 0;
}