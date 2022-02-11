#include<bits/stdc++.h>
using namespace std;

vector<bool> subsetSum(vector<int> num, vector<int> query)
{
    int N = query.size();
    // your code goes here
    vector<bool> r;
    bitset<32> boolSet;
    boolSet[0] = 1;
    for(int x : num){
        boolSet = boolSet | (boolSet<<x);
    }
    
    for(int x : query){
        r.push_back(boolSet[x]);
    }
    return r;
}