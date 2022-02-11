#include<bits/stdc++.h>
using namespace std;

int earthLevel(int k)
{
    //your code goes here
    int cnt = 0;
    while(k>0){
        k = k & (k-1);
        cnt++;
    }
    return cnt;
}