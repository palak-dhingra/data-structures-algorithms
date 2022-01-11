#include <bits/stdc++.h>
using namespace std;

int countSubArrayXOR(vector<int>arr, int k){
    int count = 0;
    int prefixXor = 0;
    unordered_map<int, int> mpp;
    for(auto x : arr){
        prefixXor = prefixXor ^ x;
        if(prefixXor==k){
            count++;
        }

        if(mpp.find(prefixXor ^ k)!=mpp.end()){
            count += mpp[prefixXor ^ k];
        }
        mpp[prefixXor]++;

    }
    return count;
}

int main() {
	vector<int> arr = { 4, 2, 2, 6, 4 };
    int k = 6;
    cout<<countSubArrayXOR(arr, k)<<endl;
	return 0;
}

