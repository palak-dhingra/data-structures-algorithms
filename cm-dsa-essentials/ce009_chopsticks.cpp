#include<bits/stdc++.h>
using namespace std;

int pairSticks(vector<int> length, int D)
{
    // your code goes here
    sort(length.begin(), length.end());
    int count = 0;
    
    int n = length.size();
    for(int i=0; i<n-1; i++){
        
        int j = i+1;
        
        if(length[j]-length[i] <= D){
            count++;
            while(j+1<n and length[j]!=length[j+1]){
                j++;
            }
        }
        
        while(i+1<n and length[i]==length[i+1]){
            i++;
        }
        
    }
    return count;
    
}