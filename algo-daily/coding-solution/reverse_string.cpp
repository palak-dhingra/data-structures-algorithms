#include <bits/stdc++.h>
using namespace std;

string reverse(string input){
	int n = input.length()-1;
	int i = 0;
	while(i<n){
		swap(input[i], input[n]);
		i++;
		n--;
	}
	return input;

}

int main() {
	string input;
	getline(cin, input);
	cout<<"input- "<<input<<endl;
	cout<<"reversed input - "<<reverse(input)<<endl;

	return 0;
}

