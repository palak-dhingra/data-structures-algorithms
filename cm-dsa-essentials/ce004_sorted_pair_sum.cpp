#include<bits/stdc++.h>
using namespace std;

pair<int, int> closestSum(vector<int> arr, int x){
    // your code goes here
    pair<int, int> result;
    int n = arr.size();
    int min_sum = INT_MAX;
    int s=0, e=n-1;
    while(s<e){
        int sum = arr[s] + arr[e];
        if( abs(sum-x) < abs(x-min_sum) ){
            result.first = arr[s];
            result.second = arr[e];
            min_sum = sum;
        }
        if(sum == x){
            return {arr[s], arr[e]};
        }
        else if(sum < x){
            s++;
        }
        else{
            e--;
        }
    }
    return result;
}