class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set()
        
        for ele in nums:
            nums_set.add(ele)
            
        max_count = 0
        
        for ele in nums:
            
            count = 0
            prev_ele = ele-1
            if not prev_ele in nums_set:
                while ele in nums_set:
                    ele += 1
                    count +=1
                    
            max_count = max(max_count, count)
            
        return max_count
        