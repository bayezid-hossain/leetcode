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

        # result=[]
        # temp=[]
        # spacePointer=0
        # length=len(s)
        # for i in range(length):
        #     if spacePointer==len(spaces):
        #         temp.append(s[i])
        #         continue
        #     if i==spaces[spacePointer]:
        #         result.append("".join(temp))
        #         temp=[s[i]]
        #         spacePointer+=1
        #     else:
        #         temp.append(s[i])
        # result.append("".join(temp))    
        # return " ".join(result)
        index, result = 0, []

        for space in spaces:
            result.append(s[index : space])
            index = space
        
        result.append(s[index :])
        return " ".join(result)