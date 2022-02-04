#include<bits/stdc++.h>
using namespace std;


int compress(vector<char>& chars) {
    // your code goes here
    string temp;
    
    int n = chars.size();
    int i = 0;
    while(i<n){
        int count = 1;
        while(i+1<n and chars[i]==chars[i+1]){
            count++;
            i++;
        }
       temp += chars[i];
       if(count>1){
           temp += to_string(count);
       }
       i++;
        
    }
    
    return temp.size();
        
}