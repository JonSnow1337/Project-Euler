/*  Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

*/

#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    const int sum = 1000;
    unsigned int result;        // this will be the solution

    for(int i=0;i<sum/2;i++){
        for(int j=0;j<sum/2;j++){
            int c = sum - i - j;
            if(i*i + j*j == c*c){
                result = i*j*c;
                break;
             }
        }
    }

    cout<<result<<endl;         // display the result
    return 0;
}
