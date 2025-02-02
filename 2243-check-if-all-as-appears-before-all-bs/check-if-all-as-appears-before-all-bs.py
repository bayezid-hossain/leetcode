class Solution:
    def checkString(self, s: str) -> bool:
        n=len(s)

        index=0
        while index<n and s[index]=='a':
            index+=1
        if index==n:
            return True
        # print(index)
        for i in range(index,n):
            if s[i]=='a':
                return False
        return True