class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        i=startIndex
        j=startIndex
        res=0
        found=False
        if words[startIndex]==target:
            return 0
        for _ in range(len(words)//2):
            i=i-1
            j=j+1

            if i==-1:
                i=len(words)-1

            if j==len(words):
                j=0
            res+=1

            if words[i]==target or words[j]==target:
                found=True
                break
        
        return res if found else -1
        