class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        arr_dict = {}
        count = 0
        for i in arr:
            comp = k-i
            if comp in arr_dict:
                count+= arr_dict[comp]
            
            if i in arr_dict:
                arr_dict[i] +=1
            else:
                arr_dict[i] = 1
        return count