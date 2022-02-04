#include <bits/stdc++.h>
using namespace std;

vector<int> uniques(vector<int>arr){
    vector<int> result;
    unordered_set<int> set_result;
    for(auto x : arr){
        if(set_result.find(x)==set_result.end()){
            set_result.insert(x);
            result.push_back(x);
        }
    }

    return result;
}
int main() {
	// your code goes here
    vector<int> arr = {1, 3, 4, 4, 5, 8, 4, 2, 2};
    vector<int> result = uniques(arr);
    for(auto x : result){
        cout<<x<<" ";
    }
	return 0;
}

