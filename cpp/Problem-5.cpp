/*  Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

*/

#include <iostream>

using namespace std;


bool isNumberDivisible(int number){
    bool isDivisible = true;
    for(int i=1; i<=20;i++){
        if(number%i != 0){
            isDivisible = false;
            break;
        }
    }

    return isDivisible;
}


int main()
{
    unsigned int number = 1;
    unsigned int smallestDivisibleNumber; // this will be the solution


    while(true){
        if(isNumberDivisible(number)){
            smallestDivisibleNumber = number;   // number is divisible by all 19 numbers, this is the solution
            break;                              // break the loop
        }else{
            number++;                           // number is not divisible, increase it by 1 and re-run the loop
        }
    }


    cout<<smallestDivisibleNumber<<endl;     // display the result
    return 0;
}
