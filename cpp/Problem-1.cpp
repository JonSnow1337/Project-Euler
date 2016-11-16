/*  Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

*/
#include <iostream>

using namespace std;

int main()
{
    int _sum = 0;

	for (int i = 1; i < 1000; i++) {
		if (i % 5 == 0) {
			// its dividable by 3 or 5
			_sum += i;
		}
		else if (i % 3 == 0) {
			_sum += i;
		}else {
			// it's not dividable by 3 or 5, skip this number

		}
	}

	cout << _sum << endl;
    return 0;
}
