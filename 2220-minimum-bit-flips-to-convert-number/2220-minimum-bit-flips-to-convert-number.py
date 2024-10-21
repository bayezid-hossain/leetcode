class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bits=(bin(start)[2:].zfill(32)[::-1])
        goal_bits=(bin(goal)[2:].zfill(32)[::-1])
        res=0
        for a,b in zip(start_bits,goal_bits):
            if a!=b:
                res+=1
        return res
        