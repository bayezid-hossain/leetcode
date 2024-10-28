class Solution:
    def numSub(self, s: str) -> int:
        inc=0
        result=0
        for c in s:
            if c=='1':
                inc+=1
            else:
                result+=((inc*(inc+1))//2)
                inc=0

        result+=((inc*(inc+1))//2)
        return int(result%(10e8+7))