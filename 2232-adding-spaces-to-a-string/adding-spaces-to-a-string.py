class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
#         result=""
        
#         spacePointer=0
#         length=len(s)
#         for nextSpace in spaces:
#             temp=""
#             for j in range(spacePointer,nextSpace):
#                 temp+=s[j]

#             spacePointer=nextSpace
#             result+=temp+" "
            
#         result+=s[spacePointer:]
#         return result

        result=""
        temp=""
        spacePointer=0
        length=len(s)
        for i in range(length):
            if spacePointer==len(spaces):
                break
            if i==spaces[spacePointer]:
                result+=temp+" "
                temp=s[i]
                spacePointer+=1
            else:
                temp+=s[i]
                
        return result+s[spaces[-1]:]