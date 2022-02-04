#include<bits/stdc++.h>
using namespace std;


void merge_row(vector<vector<int>> &v, int row, int sc, int ec){
    int mc = (sc+ec)/2;
    vector<int> temp;
    int i = sc;
    int j = mc+1;
    while(i<=mc and j<=ec){
        if(v[row][i]<v[row][j]){
            temp.push_back(v[row][i++]);
        }
        else{
            temp.push_back(v[row][j++]);
        }
    }
    while(i<=mc){
        temp.push_back(v[row][i++]);
    }
    while(j<=ec){
        temp.push_back(v[row][j++]);
    }
    int k = 0;
    for(int i=sc; i<=ec; i++){
        v[row][i] = temp[k++];
    }
}

void merge_col(vector<vector<int>> &v, int col, int sr, int er){
    int mr = (sr+er)/2;
    vector<int> temp;
    int i = sr;
    int j = mr+1;
    while(i<=mr and j<=er){
        if(v[i][col]<v[j][col]){
            temp.push_back(v[i++][col]);
        }
        else{
            temp.push_back(v[j++][col]);
        }
    }
    while(i<=mr){
        temp.push_back(v[i++][col]);
    }
    while(j<=er){
        temp.push_back(v[j++][col]);
    }
    int k = 0;
    for(int i=sr; i<=er; i++){
        v[i][col] = temp[k++];
    }
    
}
void merge(int sr, int er, int sc, int ec, vector<vector<int>> &v){
    // to sort rows
    for(int i=sr; i<=er; i++){
        merge_row(v, i, sc, ec);
    }
    
    // to sort columns
    for(int i=sc; i<=ec; i++){
        merge_col(v, i, sr, er);
    }
}
void merge_sort(int sr, int er, int sc, int ec, vector<vector<int>> &v){
    if(sr>=er and sc>=ec){
        return;
    }
    
    int mr = (sr+er)/2;
    int mc = (sc+ec)/2;
    // quad 2
    merge_sort(sr, mr, sc, mc, v);
    // quad 3
    merge_sort(mr+1, er, sc, mc, v);
    // quad 1
    merge_sort(sr, mr, mc+1, ec, v);
    // quad 4 
    merge_sort(mr+1, er, mc+1, ec, v);
    
    merge(sr, er, sc, ec, v);
    
}

vector<vector<int>> mergeSort(int m, int n, vector<vector<int>> v){
    // your code goes here
    
    merge_sort(0, m-1, 0, n-1, v);
    return v;
    
}
