class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # all elements before trackNonZero are non-zeroes
        trackNonZero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp = nums[i]
                nums[i] = nums[trackNonZero]
                nums[trackNonZero] = temp
                
                trackNonZero+=1