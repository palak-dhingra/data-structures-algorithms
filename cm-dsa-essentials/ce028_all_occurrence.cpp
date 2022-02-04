#include <bits/stdc++.h>
using namespace std;


vector<int> findAllOccurences(int k, vector<int> v){
    vector<int> result;
    for(int i=0; i<v.size(); i++){
        if(v[i]==k){
            result.push_back(i);
        }
    }
    return result;
}