class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[True for _ in range(n)]
        
        p=2
        
        count=0
        while p<n:
            if prime[p]:
                count+=1
                for i in range(p*p,n,p):
                    prime[i]=False
            p+=1
            
        return count