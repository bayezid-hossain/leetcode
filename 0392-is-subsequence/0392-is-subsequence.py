class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if t=="" and s=="":
            return True
        elif t=="":
            return False
        elif s=="":
            return True
        left=0
        right=0
        n=len(s)

        while right<len(t):
            if t[right]==s[left]:
                n-=1
                left+=1
            if n==0:
                return True
            right+=1
        return False