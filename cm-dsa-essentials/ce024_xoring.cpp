#include<bits/stdc++.h>
using namespace std;

int xoring(vector<int> v)
{
    // your code goes here
    int ans = 0;
    for(int x : v){
        ans ^= x;
    }
    return ans;

    
}