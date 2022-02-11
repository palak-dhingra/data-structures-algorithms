class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # transpose matrix
        for i in  range(rows):
            for j in range(i,cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # reverse each row
        for i in range(rows):
            j = 0
            k = cols-1
            
            while j<k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j +=1
                k -=1
                
        
        