class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        length1=len(str1)
        length2=len(str2)
        if length2>length1:
            return False
        pointerSub=0
        pointerMain=0
        while pointerMain<length1 and pointerSub<length2:
            if str1[pointerMain]==str2[pointerSub]:
                pointerMain+=1
                pointerSub+=1
                continue
            else:
                summation=(ord(str1[pointerMain])+1)-97
                summation=summation%26
                nextChar=chr(summation+97)
                if nextChar==str2[pointerSub]: 
                    pointerMain+=1
                    pointerSub+=1
                    continue
            pointerMain+=1
        return True if pointerSub==length2 else False

            