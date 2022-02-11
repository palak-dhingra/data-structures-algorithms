class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        
        sr = 0
        er = r
        sc = 0
        ec = c
        ans = []
        k = 0
        while(sr<er and sc<ec):
            # print 1st row
            for c in range(sc, ec):
                ans.append(matrix[sr][c])
             
            sr +=1 
            # print last col
            for r in range(sr, er):
                ans.append(matrix[r][ec-1])
            
            ec -=1
                
                
            if(sr<er):
                # print last row
                for c in range(ec-1, sc-1, -1):
                    ans.append(matrix[er-1][c])
                
                er -=1
            if(sc<ec):
                # print first col
                for r in range(er-1, sr-1, -1):
                    ans.append(matrix[r][sc])
                sc+=1
                
            
        return ans