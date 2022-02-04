#include <bits/stdc++.h>
using namespace std;

int search(vector<int>&v, int s, int e, int x){
    if(s>e){
        return -1;
    }
    
    int mid = (s+e)/2;
    if(v[mid]==x){
        return mid;
    }
    else if(v[mid]<x){
        return search(v, mid+1, e, x);
    }
    return search(v, s, mid-1, x);
}
  
int binarySearch(vector<int> v, int x)
{
    // your code goes here
    int n = v.size()-1;
    return search(v, 0, n, x);
    
}