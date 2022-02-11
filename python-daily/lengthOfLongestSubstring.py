class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s_dict = dict()
        l = 0 
        r = 0
        n = len(s)-1
        cnt = 0 
        while r<=n:
            if s[r] in s_dict:
                l = max(s_dict[s[r]]+1, l)
            
            s_dict[s[r]] = r
            
            cnt = max(cnt, r-l+1)
            r+=1
        return cnt
        
        