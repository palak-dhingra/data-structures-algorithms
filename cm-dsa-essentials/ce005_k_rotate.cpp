#include<bits/stdc++.h>
using namespace std;

void reverse(vector<int> &a, int s, int e){
    while(s<e){
        swap(a[s++], a[e--]);
    }
}

vector<int> kRotate(vector<int> a, int k){
    // your code  goes here
    int s = 0;
    int e = a.size() - 1;
    reverse(a, s, e);
    reverse(a, s, k-1);
    reverse(a, k, e);
    return a;    
}