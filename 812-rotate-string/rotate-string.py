class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal)!=len(s):
            return False
        s=s*2
        if goal in s:
            return True
        else:
            return False