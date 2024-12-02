class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        length=len(pref)
        for word in words:
            first,second=0,0
            length2=len(word)
            while second<length and first<length2 and word[first]==pref[second]:
                first+=1
                second+=1
            if second==length:
                count+=1
        return count