class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ans = 0
        curr_max = 0
        for i in nums:
            if i==1:
                curr_max +=1
                max_ans = max(max_ans, curr_max)
            else:
                curr_max = 0
                
        return max_ans
        