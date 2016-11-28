/*  Problem 14

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

*/



#include <iostream>
#include <vector>

using namespace std;



struct CollatzNumber{
    long long int number;
    long long int chainCount;
};


long long int CalculateChainCount(long long int number){
    long long int _count(1);

    // run a loop for so long untill the number reaches 1, then return the count
    while(true){
        if(number == 1){
            return _count;
        }

        if(number % 2 == 0){            // even number
            number = number / 2;
        }else{
            number *= 3;    // odd number
            number += 1;
        }
        _count++;
    }
}

int main()
{
    vector<CollatzNumber> sequence;
    long long int _number;                    // this will be the solution

    // populate the Collatz sequence with numbers from 1 to 1M
    for(int i=1;i<=1000000;i++){
        long long int num(i);
        long long int chainCount;
        chainCount = CalculateChainCount(num);

        // once the calculation is done, add the number and its chain count to the sequence vector
        CollatzNumber cnumber;
        cnumber.number = num;
        cnumber.chainCount = chainCount;
        sequence.push_back(cnumber);

    }


    long long int biggestChain = 0;
    for(int i=0;i<sequence.size();i++){
        if(sequence[i].chainCount > biggestChain){
            _number = sequence[i].number;
            biggestChain = sequence[i].chainCount;
        }
    }

    cout<<_number<<endl;

    return 0;
}
