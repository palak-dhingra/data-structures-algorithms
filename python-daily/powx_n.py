class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        ans = 1.0
        if n<0 :
            nm = -1*n 
        else:
            nm = n
        while nm>0:
            rem = nm%2
            if rem==0:
                x = x*x
                nm = nm//2
        
            else:
                ans = ans *x
                nm -=1
                
        if n<0:
            return 1/ans
        
        return ans