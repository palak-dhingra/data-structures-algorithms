#include<bits/stdc++.h>
using namespace std;

int defkin(int W, int H, vector<pair<int, int>> position)
{
    // your code goes here
    int n = position.size();
    vector<int> x(n, 0);
    vector<int> y(n, 0);
    
    for(int i=0; i<n; i++){
        x[i] = position[i].first;
        y[i] = position[i].second;
    }
    sort(x.begin(), x.end());
    sort(y.begin(), y.end());
    
    int x_diff = x[0]-1;
    int y_diff = y[0]-1;
    for(int i=1; i<n; i++){
        x_diff = max(x_diff, x[i]-x[i-1]-1);
        y_diff = max(y_diff, y[i]-y[i-1]-1);
    }
    
    x_diff = max(x_diff, W-x[n-1]);
    y_diff = max(y_diff, H-y[n-1]);
    return x_diff*y_diff;
    
}