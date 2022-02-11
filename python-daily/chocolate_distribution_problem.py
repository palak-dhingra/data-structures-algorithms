class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        # M is the no. of students to pick
        # N is the no. if chocolates
        if M==0 or N==0:
            return 0
        
        if M > N:
            return -1
            
        A.sort()
        
        min_diff = A[N-1] - A[0]
        
        for i in range(len(A) - M + 1):
            min_diff = min(min_diff, A[i+M-1] - A[i])
        
        return min_diff