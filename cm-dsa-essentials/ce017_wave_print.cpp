#include<bits/stdc++.h>
using namespace std;
 
 vector<int> WavePrint(int m, int n, vector<vector<int>> arr)
{
    // your code goes here
    vector<int> result;
    int rows = arr.size();
    int cols = arr[0].size()-1;
    while(cols>=0){
        int startRow = 0;
        while(startRow<rows){
            result.push_back(arr[startRow++][cols]);
        }
        
        startRow = rows-1;
        cols--;
        while(cols>=0 and startRow>=0){
            result.push_back(arr[startRow--][cols]);
        }
        cols--;
    }
    return result;
    
}
