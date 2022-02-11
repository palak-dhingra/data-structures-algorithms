class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for x in s:
            if (x>='a' and x<='z') or(x>='A' and x<='Z') or (x>='0' and x<='9'):
                temp +=x
        temp = temp.lower()
        reverse_temp = temp[::-1]
        
        return reverse_temp==temp
        