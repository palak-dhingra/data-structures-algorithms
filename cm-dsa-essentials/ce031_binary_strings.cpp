#include <bits/stdc++.h>
using namespace std;

void generate(int n, vector<string>&result, string word){
    if(n==1){
        result.push_back(word);
        return;
    }
    
    generate(n-1, result, word+"0");
    int len=word.length();
    if(word[len-1]=='1'){
        return;
    }
    generate(n-1, result, word+"1");
    
}

vector<string> binaryStrings(int n){
    // do not modify any default function or parameter you can use helper function if needed
    vector<string> result;
    generate(n, result, "0");
    generate(n, result, "1");
    return result;
    
}