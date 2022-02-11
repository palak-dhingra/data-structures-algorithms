class Solution:
    def maxLen(self, n, arr):
        #Code here
        max_count = 0
        prefix_sum = 0
        arr_dict = dict()
        
        for i in range(n):
            prefix_sum += arr[i]
            
            if prefix_sum==0:
                max_count = max(max_count, i+1)
            
            elif prefix_sum in arr_dict:
                max_count = max(max_count, i-arr_dict[prefix_sum])
            else:
                arr_dict[prefix_sum] = i
            
        return max_count