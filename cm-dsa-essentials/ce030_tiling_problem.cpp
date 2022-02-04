#include <iostream>
using namespace std;

int tillingProblem(int n, int m){
    // base case
    if(n==0){
        return 1;
    }
    if(n<0){
        return 0;
    }
    
    return tillingProblem(n-1, m) + tillingProblem(n-m, m);
}