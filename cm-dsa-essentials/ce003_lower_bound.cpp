#include<bits/stdc++.h>
using namespace std;


int lowerBound(vector<int> A, int Val) {
    // your code goes here
    int n = A.size();
    int s = 0;
    int e = n-1;
    while(s<=e){
        int mid = (s+e)/2;
        if(A[mid]==Val){
            return Val;
        }
        else if(A[mid]<Val){
            s = mid+1;
        }
        else{
            e = mid-1;
        }
    }
    if(e>=0){
        return A[e];
    }
    return -1;
    
}