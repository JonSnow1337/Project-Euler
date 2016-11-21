/*  Problem 11



In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

(Grid is saved in resources/prob011_grid.txt)

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?


*/



#include <iostream>
#include <vector>
#include <fstream>

using namespace std;


int main()
{
    int grid[20][20];              // Grid (a 2D array of integers)
    unsigned long long int _solution = 0;   // this will be the solution

    ifstream file_input("resources\\prob011_grid.txt");

    if(!file_input){
        cout<<"File prob011_grid.txt is missing from the resource folder"<<endl;
        return 1;
    }

     // populate the array from the text file
    for(int i=0;i<20;i++){
        for(int j=0;j<20;j++){
            file_input >> grid[i][j];
        }
    }

    // run every combination (up, down, diagonal) and compare it to the biggest found product, once the biggest number is found, display it on the screen

    // left to right
    unsigned int temp;

    //temp = grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3];

    // left to right
    for(int i=0;i<20;i++){
        int j=3;
        while(j<20){
            temp = grid[i][j-3] * grid[i][j-2] * grid[i][j-1] * grid[i][j];
            if(temp > _solution){
                _solution = temp;
            }
            j++;
        }
    }

    // top to bottom
    for(int j=0;j<20;j++){
        int i=3;
        while(i<20){
            temp = grid[i-3][j] * grid[i-1][j] * grid[i-1][j] * grid[i][j];
            if(temp > _solution){
                _solution = temp;
            }
            i++;
        }
    }



    // diagonal to the right
    for(int i=0;i<17;i++){
        for(int j=0;j<17;j++){
            temp = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3];
            if(temp > _solution){
                _solution = temp;
            }
        }
    }


    // diagonal to the left
    for(int i=3;i<20;i++){
        for(int j=3;j<20;j++){
            temp = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3];
            if(temp > _solution){
                _solution = temp;
            }
        }
    }


    cout<<_solution<<endl;      // display the solution
    return 0;
}
