class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<=1:
            return s 
        result=[]
        last_count=0
        for c in s:
            if len(result)==0 or result[-1]==c :
                last_count+=1
            else:
                last_count=1
            if last_count<3:
                result.append(c)
        return ''.join(result)