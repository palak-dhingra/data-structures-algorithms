#include<bits/stdc++.h>
using namespace std;

vector<int> sortingWithComparator(vector<int> a, bool flag){
    // your code  goes here
    sort(a.begin(), a.end());
    if(!flag){
        reverse(a.begin(), a.end());
    }
    return a;
    
}