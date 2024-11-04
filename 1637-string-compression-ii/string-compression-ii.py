class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        getLength=lambda x: 1 if x<2 else 2 if x<10 else 3 if x<100 else 4
        @cache
        def recursion(start,k):
            if start<0:
                return 0
            result=recursion(start-1,k-1) if k else 9e9

            frequency=0
            for j in range(start,-1,-1):
                if s[j]==s[start]:
                    frequency+=1
                elif k==0:
                    return result
                else:
                    k-=1
                result=min(result,recursion(j-1,k)+getLength(frequency))
                # print(result)
            return result

        
        return recursion(len(s)-1,k)