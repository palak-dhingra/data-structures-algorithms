#include<bits/stdc++.h>
using namespace std;

bool compare(pair<int,int> a, pair<int,int> b){
    float dis_a = sqrt(a.first*a.first + a.second*a.second);
    float dis_b = sqrt(b.first*b.first + b.second*b.second);
    return dis_a < dis_b;
}

vector<pair<int,int>> sortCabs(vector<pair<int,int>> v){
    // your code  goes here
    sort(v.begin(), v.end(), compare);
    return v;
}