#include <bits/stdc++.h>
using namespace std;

string removeDuplicate(string s){
    // your code goes here
    string ns;
    vector<int> freq_s(26, 0);
    for(char c : s){
        freq_s[c-'a']++;
    }
    
    for(int i=0; i<26; i++){
        if(freq_s[i]!=0){
            ns += 'a'+i;
        }
    }
    return ns;
    
}