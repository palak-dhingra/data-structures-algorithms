class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_len = len(nums1)-1
        m = m-1
        n = n-1
        while m>=0 and n>=0:
            if nums2[n] >= nums1[m]:
                nums1[num1_len] = nums2[n]
                n -=1
            else:
                nums1[num1_len] = nums1[m]
                m -=1
                
            num1_len -=1
            
        while n>=0:
            nums1[num1_len] = nums2[n]
            n -=1
            num1_len -=1
        