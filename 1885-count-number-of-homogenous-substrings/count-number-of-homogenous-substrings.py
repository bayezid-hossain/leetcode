class Solution:
    def countHomogenous(self, s: str) -> int:
        last_char=s[0]
        word_map={}
        inc=0
        result=0
        for c in s:
            if last_char==c:
                inc+=1
            else:
                result+=((inc*(inc+1))//2)
                inc=1
                last_char=c
        
        result+=((inc*(inc+1))//2)
        return int(result%(10e8+7))
            



