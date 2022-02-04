#include<bits/stdc++.h>
using namespace std;

void rotate(vector<vector<int>>& matrix) {
      // your code goes here
      int rows = matrix.size();
      int cols = matrix[0].size();
      
      for(int i=0; i<rows; i++){
          for(int j=0; j<i; j++){
              swap(matrix[i][j], matrix[j][i]);
          }
      }
      
      for(int i=0; i<rows; i++){
          int s = 0;
          int e = cols-1;
          while(s<e){
              swap(matrix[i][s++], matrix[i][e--]);
          }
      }
}
