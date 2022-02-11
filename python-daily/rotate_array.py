class Solution:
    def reverse_arr(self, nums: List[int], s: int, e: int) -> None:
        while(s<e):
            temp = nums[s]
            nums[s] = nums[e]
            nums[e] = temp
            s+=1
            e-=1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        self.reverse_arr(nums, 0, n-1)
        self.reverse_arr(nums, 0, k-1)
        self.reverse_arr(nums, k, n-1)