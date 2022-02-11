class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        sr = 0
        sc = cols-1
        while(sr<rows and sc>=0):
            if(matrix[sr][sc]==target):
                return True
            elif(matrix[sr][sc]<target):
                sr +=1
            else:
                sc -=1
        
        return False
        