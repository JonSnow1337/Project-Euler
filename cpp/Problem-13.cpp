/*  Problem 13

    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    the numbers are saved in a file called: prob013_nums.txt
*/


/*
    For this problem we're using a big integer library by panks
    https://github.com/panks/BigInteger

    It's used to store the 50 digit numbers
    only BigIntegerSingleFile.cpp is required
*/

#include <iostream>
#include <fstream>
#include "libs/BigInteger/BigIntegerSingleFile.cpp"

using namespace std;

int main()
{
    ifstream infile("resources\\prob013_nums.txt");
    BigInteger currentNum(10);
    BigInteger _totalSum = 0;
    string s;
    while (infile >> s)
    {
        currentNum = s;
        _totalSum += currentNum;
    }



    cout<<_totalSum.getNumber()<<endl;     // display the result
    return 0;
}
