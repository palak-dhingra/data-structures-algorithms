#include<bits/stdc++.h>
using namespace std;

vector<int> optimizedBubbleSort(vector<int> v){
    // your code  goes here
    int n = v.size();
    
    for(int i=0; i<n-1; i++){
        bool isSwapped = false;
        for(int j=0; j<n-i-1; j++){
            if(v[j] > v[j+1]){
                swap(v[j], v[j+1]);
                isSwapped = true;
            }
        }
        if(!isSwapped){
            break;
        }
    }
    return v;
    
}