#include <iostream>
using namespace std;
 
 
int power(int x, int y, int mod)
{
    // your code goes here
    x = x%mod;
    int ans = 1;
    while(y>0){
        int last_digit = (y&1);
        if(last_digit){
            ans = (ans*x)%mod;
        }
        y = y>>1;
        x = (x*x)%mod;
    }
    return ans;
    
}