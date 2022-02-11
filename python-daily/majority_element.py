class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        m_e = None
        for ele in nums:
            if count == 0:
                m_e = ele
                
            if m_e == ele:
                count +=1
            else:
                count -=1
                
        return m_e