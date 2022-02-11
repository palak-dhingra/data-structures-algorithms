class Solution:
        
	def rowWithMax1s(self,arr, n, m):
		R = len(arr)
		C = len(arr[0])
		max_row_index = 0
		index = C-1
		
		for i in range(0, R):
		    oneFound = False
		    while(index >=0 and arr[i][index]==1):
		        oneFound = True
		        index -=1
		        
		    if(oneFound):
		        max_row_index = i
		
	    if max_row_index==0 and arr[0][C-1]==0:
	        return -1
		
		return max_row_index