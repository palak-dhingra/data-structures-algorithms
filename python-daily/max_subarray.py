class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        
        curr_sum = 0
        for ele in nums:
            curr_sum += ele
            max_sum = max(max_sum, curr_sum)
            if curr_sum<0:
                curr_sum = 0
        return max_sum
        