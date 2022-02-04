#include<bits/stdc++.h>
using namespace std;

string vowel(string S){
    // your code goes here
    string ns;
    for(char c : S){
        if(c=='a' or c=='i' or c=='e' or c=='o' or c=='u'){
            ns += c;
        }
    }
    return ns;
    
} 