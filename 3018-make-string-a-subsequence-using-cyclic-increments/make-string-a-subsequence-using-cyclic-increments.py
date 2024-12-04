class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        length1=len(str1)
        length2=len(str2)
        if length2>length1:
            return False
        pointerSub=0
        pointerMain=0
        while pointerMain<length1 and pointerSub<length2:
            cur_main=str1[pointerMain]
            next_sub=str2[pointerSub]
            if cur_main==next_sub or chr((((ord(cur_main)+1)-97)%26)+97)==next_sub:
                pointerSub+=1
            
            pointerMain+=1
        return True if pointerSub==length2 else False

            
