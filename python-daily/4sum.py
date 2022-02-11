class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        i = 0
        j = i+1
        
        while i<n:
            j = i+1
            while j<n:
                two_sum = target - (nums[i] + nums[j])
                left = j+1
                right = n-1
                while(left<right):
        
                    lr_sum = nums[left] + nums[right]
                    if (two_sum ==lr_sum):
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        front = nums[left]
                        back = nums[right]
                        while left<right and nums[right]==back:
                            right-=1
                        while left<right and nums[left]==front:
                            left +=1
                        
                    elif lr_sum < two_sum:
                        left +=1
                    else:
                        right-=1
                
                if(j+1==n):
                    break;
                j+=1
                while j+1<n and nums[j]==nums[j-1]:
                    j +=1
                
            if i+1==n:
                break;
            i+=1
            while i+1<n and nums[i]==nums[i-1]:
                i +=1
                
            
            
        return result
                        
        