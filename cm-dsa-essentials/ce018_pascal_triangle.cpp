#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> printPascal(int n)
{
    // your code goes here
    vector<vector<int>> result;
    
    result.push_back({1});
    int i=1;
    while(i<n){
        vector<int> temp;
        temp.push_back(1);
        
        int j = 1;
        while(j<i){
            temp.push_back(result[i-1][j-1]+ result[i-1][j]);
            j++;
        }
        
        temp.push_back(1);
        result.push_back(temp);
        i++;
    }
    return result;
    
    
}
 



