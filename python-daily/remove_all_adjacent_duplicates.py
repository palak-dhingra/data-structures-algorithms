class Solution:
    def removeDuplicates(self, s: str) -> str:
        temp = ""
        i = 0;
        for x in s:
            if i>0 and temp[i-1]==x:
                temp = temp[:i-1]
                i = i-1
            else:
                temp +=x
                i = i + 1
        return temp