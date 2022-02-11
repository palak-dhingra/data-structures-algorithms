class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums, s, e):
            inv = 0
            if(s>=e):
                return inv
            mid = (s+e)//2
            inv += mergeSort(nums, s, mid)
            inv += mergeSort(nums, mid+1, e)
            inv += merge(nums, s, e)
            
            return inv
        def merge(nums, s, e):
            mid = (s+e)//2
            j = mid +1
            cnt = 0
            for i in range(s, mid+1):
                while j<=e and nums[i] > 2*nums[j]:
                    j +=1
                cnt += j - (mid+1)
                
            temp = []
            
            i = s
            j = mid+1
            while i<=mid and j<=e:
                if nums[i]<nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            while i<=mid:
                temp.append(nums[i])
                i+=1
            while j<=e:
                temp.append(nums[j])
                j+=1
                
            k = s
            for i in temp:
                nums[k] = i
                k+=1
            return cnt
        
        s = 0
        e = len(nums)-1
        return mergeSort(nums, s, e)