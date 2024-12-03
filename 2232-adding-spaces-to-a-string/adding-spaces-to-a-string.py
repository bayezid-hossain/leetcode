class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result=""
        
        spacePointer=0
        
        for nextSpace in spaces:
            temp=""
            for j in range(spacePointer,nextSpace):
                temp+=s[j]

            spacePointer=nextSpace
            result+=temp+" "
            
        result+=s[spacePointer:]
        return result