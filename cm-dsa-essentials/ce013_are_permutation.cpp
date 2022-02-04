#include <bits/stdc++.h>
using namespace std;
 
bool arePermutation(string A, string B)
{
    int n_a = A.size();
    int n_b = B.size();
    if(n_a!=n_b){
        return false;
    }
    // your code goes here
    vector<int> freq_a(26, 0);
    vector<int> freq_b(26, 0);
    for(int i=0; i<n_a; i++){
        freq_a[A[i]- 'a']++;
        freq_b[B[i]- 'a']++;
    }
    
    for(int i=0; i<26; i++){
        if(freq_a[i]!=freq_b[i]){
            return false;
        }
    }
    return true;
}