class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = 0
        cand1 = 0
        c2 = 0
        cand2 = 0
        
        for x in nums:
            if x==cand1:
                c1 +=1
            elif x==cand2:
                c2 +=1
            elif c1==0:
                cand1 = x
                c1 = 1
            elif c2==0:
                cand2 = x
                c2 = 1
            else:
                c1 -=1
                c2 -=1
                
        
        freq1 = 0
        freq2 = 0
        for x in nums: 
            if x==cand1:
                freq1 +=1
            elif x==cand2:
                freq2 +=1
        
        n = len(nums)
        result = []
        if freq1 > n/3:
            result.append(cand1)
        if cand1!=cand2 and freq2 > n/3:
            result.append(cand2)
            
        return result
                
                
        