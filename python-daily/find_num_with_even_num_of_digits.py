class Solution:
    def oddEvenDigit(self, num: int) -> bool:
        count = 0
        while num >0:
            count+=1
            num = num//10
            
        return count%2==0
    
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if Solution.oddEvenDigit(self, n):
                count +=1
        return count
        