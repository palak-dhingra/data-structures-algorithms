#include<bits/stdc++.h>
using namespace std;

bool compare(pair<string,int> a, pair<string,int> b){
    return a.second < b.second;
}

vector<pair<string,int>> sortFruits(vector<pair<string,int>> v, string S){
    // your code  goes here
    
    if(S=="name"){
        sort(v.begin(), v.end());
    }
    else if(S=="price"){
        sort(v.begin(), v.end(), compare);
    }
    return v;
}