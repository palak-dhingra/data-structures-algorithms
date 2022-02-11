class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)-1
        idx1 = n-1
        while idx1>=0 and nums[idx1+1] <= nums[idx1]:
            idx1 -=1
       
        if idx1 >=0 :
            idx2 = n
            
            while nums[idx2] <= nums[idx1]:
                idx2 -=1
                
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
        
        idx1 +=1
        # reverse elements after idx2
        while idx1<=n:
            nums[idx1], nums[n] = nums[n], nums[idx1]
            idx1 +=1
            n -=1