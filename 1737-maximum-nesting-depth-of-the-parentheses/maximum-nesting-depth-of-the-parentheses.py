class Solution:
    def maxDepth(self, s: str) -> int:
        max_len=0
        cur=0

        for c in s:
            if c=="(":
                cur+=1
            elif c==")":
                max_len=max(max_len,cur)
                cur-=1
        return max_len