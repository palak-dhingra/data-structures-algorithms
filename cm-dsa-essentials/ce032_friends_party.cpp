#include <bits/stdc++.h>
using namespace std;

int friendsPairing(int n){
    
    if(n==0 or n==1){
        return 1;
    }
    if(n<0){
        return 0;
    }
    
    return friendsPairing(n-1) + (n-1)*friendsPairing(n-2);
    
}