/*  Problem 6

The sum of the squares of the first ten natural numbers is,

12^2 + 22^2 + ... + 102^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

*/

#include <iostream>

using namespace std;

int main()
{
    int _sumOfSquares = 0;  // set up the sum variables to 0
    int _squareOfSum = 0;
    int difference;         // this will the the solution

    int regularSum = 0;     // will contain the sum of all numbers (without any squares)
    // Iterate through numbers 1 to 100
    for(int i=1 ; i<=100 ; i++){
        _sumOfSquares += i*i;
        regularSum += i;
    }


    _squareOfSum = regularSum * regularSum;         // square the regular sum
    difference = _squareOfSum - _sumOfSquares;      // get the difference

    cout<<difference<<endl;     // display the result
    return 0;
}
