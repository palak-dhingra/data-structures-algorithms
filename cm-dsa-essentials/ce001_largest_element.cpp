#include<bits/stdc++.h>
using namespace std;

int largestElement(vector<int> arr) {
    int largest = INT_MIN;
    for(int a : arr){
        largest = max(largest, a);
    }
    return largest;
     
}