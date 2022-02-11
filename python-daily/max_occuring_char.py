class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self,s):
        #code here
        t = [0]*26
        for c in s:
            idx= ord(c)-ord('a')
            t[idx]+=1
        
        max_c = 0
        c=''
        for i in range(26):
            if t[i]>max_c:
                max_c=t[i]
                c=chr(ord('a')+i)
        return c