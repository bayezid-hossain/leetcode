class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<=1:
            return s 
        result=[]
        result.append(s[0])
        last_count=1
        for c in s[1:]:
            if result[-1]==c :
                last_count+=1
                if last_count<3:
                    result.append(c)
            else:
                last_count=1
                result.append(c)
        return ''.join(result)