class Solution:
    def smallestValue(self, n: int) -> int:
        a=2
        def factorials(n,a):
            if n==1:
                return 0
            if n%a==0:
                return a + factorials(n//a,a)
            else:
                return factorials(n,a+1)
        
        sum=factorials(n,2)
        if sum==n:
            return n
        
        return self.smallestValue(sum)
        