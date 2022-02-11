#User function Template for python3
class Solution:
	def isPalindrome(self, S):
		# code here
		s = 0 
		e = len(S) -1
		while s<e:
		    if S[s]!=S[e]:
		        return 0
		    s+=1
		    e-=1
		return 1