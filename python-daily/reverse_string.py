class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        e = len(s) - 1
        b = 0
        while b<e:
            s[b], s[e] = s[e], s[b]
            b +=1
            e -=1
        
        
        