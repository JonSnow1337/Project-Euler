/*   Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

*/

//  file is located in resources\p022_names.txt


#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <istream>
#include <algorithm>



using namespace std;

// a structure that holds the name string and its multiplier (index, which is used to calculate the name score)
struct name{
    string _name;
    unsigned int _multiplier;

    name(string n, unsigned int mp){
        _name = n;
        _multiplier = mp;
    }
};

// a function used by std::sort to compare strings
bool sortByName(const name &lhs, const name &rhs) {
        //return lhs._name < rhs._name;
        if(lhs._name.compare(rhs._name) < 0){
            return true;
        }else{
            return false;
        }
}


unsigned int CalculateScoreForName(name nam){
    unsigned int totalScore = 0;
    for(int i=0;i<nam._name.size();i++){
        switch(nam._name[i]){
        case 'A':
            totalScore += 1;
            break;
        case 'B':
            totalScore += 2;
            break;
        case 'C':
            totalScore += 3;
            break;
        case 'D':
            totalScore += 4;
            break;
        case 'E':
            totalScore += 5;
            break;
        case 'F':
            totalScore += 6;
            break;
        case 'G':
            totalScore += 7;
            break;
        case 'H':
            totalScore += 8;
            break;
        case 'I':
            totalScore += 9;
            break;
        case 'J':
            totalScore += 10;
            break;
        case 'K':
            totalScore += 11;
            break;
        case 'L':
            totalScore += 12;
            break;
        case 'M':
            totalScore += 13;
            break;
        case 'N':
            totalScore += 14;
            break;
        case 'O':
            totalScore += 15;
            break;
        case 'P':
            totalScore += 16;
            break;
        case 'Q':
            totalScore += 17;
            break;
        case 'R':
            totalScore += 18;
            break;
        case 'S':
            totalScore += 19;
            break;
        case 'T':
            totalScore += 20;
            break;
        case 'U':
            totalScore += 21;
            break;
        case 'V':
            totalScore += 22;
            break;
        case 'W':
            totalScore += 23;
            break;
        case 'X':
            totalScore += 24;
            break;
        case 'Y':
            totalScore += 25;
            break;
        case 'Z':
            totalScore += 26;
            break;
        default:
            totalScore += 0;
            break;
        }
    }
    totalScore *= nam._multiplier;          // multiply the score with it's index

    return totalScore;
}

void RemoveChars(string &str){              // function that removes quotation marks around the strings
    str.erase(0, 1);
    str.erase(str.size()-1 , str.size() -2);
}

int main()
{
    vector<name> names;       // vector that contains all the names from the file
    vector<name> namesAlphabetical;
    unsigned long long int _sum = 0;

    ifstream file_input("resources\\p022_names.txt");


    if(!file_input){
        cout<<"Can not open file"<<endl;
        return 1;
    }

    string line;
    while(getline(file_input,line))
    {
        stringstream   linestream(line);
        string         value;

        while(getline(linestream,value,','))
        {
            RemoveChars(value);                 // remove quotation marks around the string
            name nam(value, 0);                 // create a temporary name object
            names.push_back(nam);               // push the name to the vector
        }
    }


    sort(names.begin(), names.end(), sortByName);

    // set each name's index equivalent to it's alphabetical position
    for(int i=0;i<names.size();i++){
        names[i]._multiplier = i + 1;
    }


    // calculate the score for each name
    for(int i=0;i<names.size();i++){
        _sum += CalculateScoreForName(names[i]);
    }

    cout<<_sum<<endl;                           // display the result
    return 0;
}
