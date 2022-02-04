#include<bits/stdc++.h>
using namespace std;


int sum(vector<vector<int>> v, int sr, int sc, int er, int ec){
    // your code goes here
    int r = v.size();
    int c = v[0].size();
    int p[r][c];
    
    p[0][0] = v[0][0];
    for(int i=1; i<r; i++){
        p[i][0] = p[i-1][0] + v[i][0];
    }
    cout<<endl;
    
    for(int i=1; i<c; i++){
        p[0][i] = p[0][i-1] + v[0][i];
    }
    
    for(int i=1; i<r; i++){
        for(int j=1; j<c; j++){
            p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + v[i][j];
        }
    }
    
    sr--;
    sc--;
    int ans = p[er][ec];
    if(sr>=0){
        ans -= p[sr][ec];
    }
    if(sc>=0){
        ans -= p[er][sc];
    }
    if(sr>=0 and sc>=0){
        ans += p[sr][sc]; 
    }
    return ans;
    
}