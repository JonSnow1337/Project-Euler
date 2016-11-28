/*   Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

*/


#include <iostream>
#include <vector>


using namespace std;


// this function checks if the number is amicable
/**
* How it works:
* 1. Sum all proper divisors of the number
* 2. Take that sum and make a sum of all of it's proper divisors
* 3. If sum2(the second one) is equal to the original number, that number is amicable. Return true
* 4. If not, the number is not amicable
*/
bool isAmicable(unsigned int number){
    unsigned long long int sum1 = 0;
    unsigned long long int sum2 = 0;

    for(unsigned int i=2;i<=number;i++){
        if(number % i == 0){
            // its a proper divisor
            sum1 += number/i;
        }
    }

    for(unsigned int i=2;i<=sum1;i++){
        if(sum1 % i == 0){
            // its a proper divisor
            sum2 += sum1/i;
        }
    }

    if(sum1 == number){
        return false;
    }

    if(sum2 == number){
        return true;
    }else{
        return false;
    }

}

int main()
{
    unsigned long long int _sum = 0;        // total sum of amicable numbers, the final solution

    // run numbers 2 through 10000 and sum them if they are amicable
    for(unsigned int i = 1;i<=10000;i++){
        if(isAmicable(i)){
            _sum += i;
        }
    }

    cout<<_sum<<endl;                       // display the result
    return 0;
}
