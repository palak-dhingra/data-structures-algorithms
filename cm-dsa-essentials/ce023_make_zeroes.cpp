#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> makeZeroes(vector<vector<int>> arr){
    // your code goes here
    int rows = arr.size();
    int cols = arr[0].size(); 
    bool col0 = false;
    for(int i=0; i<rows; i++){
        if(arr[i][0]==0){
            col0=true;
        }
        
        for(int j=1; j<cols; j++){
            if(arr[i][j]==0){
                arr[0][j] = 0;
                arr[i][0] = 0;
            }
        }
    }
    
    for(int i=rows-1; i>=0; i--){
        for(int j=cols-1; j>=1; j--){
            if(arr[0][j]==0 or arr[i][0]==0){
                arr[i][j] = 0;
            }
        }
        if(col0){
            arr[i][0] = 0;
        }
    }
    
    return arr;
}