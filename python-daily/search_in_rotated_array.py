class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while low<=high:
            mid = (low+high)//2
            
            if nums[mid]==target:
                return mid
            
            # case 1 - after mid nums is sorted
            elif nums[mid]<nums[high]:
                # case 1.1
                if nums[mid]<target and nums[high] >= target:
                    low = mid+1
                else:
                    high = mid-1
            # case 2  - before mid nums is sorted
            else:
                if nums[mid]>target and nums[low]<=target:
                    high = mid-1
                else:
                    low = mid+1
                    
        return -1