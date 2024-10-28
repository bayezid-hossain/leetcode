class Solution:
    def countHomogenous(self, s: str) -> int:
        last_char=s[0]
        word_map={}
        inc=0
        result=0
        for c in s:
            if last_char==c:
                inc+=1
                result+=inc
            else:
                inc=1
                result+=1
                last_char=c
        return int(result%(10e8+7))
            



