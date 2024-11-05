class Solution:
    def minChanges(self, s: str) -> int:
        def breakandbuild(string):
            if len(string)==2:
                return 0 if string[0]==string[1] else 1
            div=len(string)//2
            if div%2==0:
                return breakandbuild(string[:div])+breakandbuild(string[div:])
            else:
                return breakandbuild(string[:div+1])+breakandbuild(string[div+1:])
        result=breakandbuild(s)
        return result    
        