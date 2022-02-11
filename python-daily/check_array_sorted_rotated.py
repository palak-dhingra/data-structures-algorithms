class Solution:
    def check(self, nums: List[int]) -> bool:
        # array is sorted and rotated if the array is either in increasing order or the array has last element smaller than first element
        
        count = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                count+=1
        
        if nums[n-1] > nums[0]:
            count+=1
        return count<=1