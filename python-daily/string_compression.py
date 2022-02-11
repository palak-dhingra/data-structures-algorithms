class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        chars_len = len(chars)
        i = 1
        j = 1
        while i < chars_len:
            if(chars[i]==chars[i-1]):
                count+=1
            else:
                if count>1:    
                    for c in str(count):
                        chars[j] = c
                        j+=1
                    chars[j] = chars[i] 
                    j+=1
                else:
                    chars[j] = chars[i]
                    j+=1
                count = 1
                
            i+=1
        if count>1:

            for c in str(count):
                chars[j] = c
                j+=1

        return j