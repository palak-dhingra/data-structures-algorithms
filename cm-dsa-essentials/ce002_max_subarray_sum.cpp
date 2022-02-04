#include<bits/stdc++.h>
using namespace std;

int maxSumSubarray(vector<int> A) {
    int rs = A[0];
    int ms = A[0];
    int n = A.size();
    for(int i=1; i<n; i++){
        rs += A[i];
        if(rs<0){
            rs = 0;
        }else{
            ms = max(ms, rs);
        }
    }
    return ms;
    
}