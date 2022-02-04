#include <iostream>
#include <string>
using namespace std;
 
int binaryToDecimal(string s)
{
    // your code goes here
    int n = s.size()-1;
    int po = 1;
    int num = 0;
    while(n>=0){
        num += (s[n]-'0')*po;
        po*=2;
        n--;
    }
    return num;
    
}
 