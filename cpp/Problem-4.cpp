/*  Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

*/

#include <iostream>
#include <sstream>

using namespace std;



string IntToString (int a)
{
    ostringstream temp;
    temp<<a;
    return temp.str();
}

string stringBackwards(string str){
    if (str.size() == 0){
        return "error";
    }

    string strBack = "";
    for(int i=str.size() - 1 ; i>=0 ; i--){
        strBack += str[i];
    }
    return strBack;
}


bool isPalindromic(string s1, string s2){
    if(s1 == s2){
        return true;
    }else{
        return false;
    }
}


int main()
{
    int _largestPalinDrome = 0; // this will be the solution


    for(int i=100;i<=999;i++){
        for(int j=100;j<=999;j++){
            int result = i * j;
            string strResult = IntToString(result);
            string strResultBackwards  = stringBackwards(strResult);

            // check if strresult and strresultbackwards are palindromic
            if(isPalindromic(strResult, strResultBackwards)){
                // result is palindromic
                if(result > _largestPalinDrome){
                    _largestPalinDrome = result;
                }
            }else{
                // do nothing
            }
        }
    }


    cout<<_largestPalinDrome<<endl;     // display the result
    return 0;
}
