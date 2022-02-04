#include<bits/stdc++.h>
using namespace std;

void inc(int N, vector<int> &result){
    if(N==0){
        return;
    }
    inc(N-1, result);
    result.push_back(N);
}

vector<int> increasingNumbers(int N) {
    vector<int> result;
    inc(N, result);
    return result;
}