#include <bits/stdc++.h>
using namespace std;

int sum_all_primes(int n){
    vector<bool> prime_arr(n+1, true);
    // mark all non-primes false
    for(int i=2; i<n+1; i++){
        if(prime_arr[i]){
            for(int j=2*i; j<n+1; j+=i){
                prime_arr[j]=false;
            }
        }
    }

    int count = 0;
    for(int i=2; i<n+1; i++){
        if(prime_arr[i]){
            count +=i;
        }
    }
    return count;


}
int main() {
	
    int n = 55;
    cout<<sum_all_primes(n)<<endl;
	return 0;
}

