class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        result=0
        _=0
        for c in moves:
            if c=='L':result+=1
            elif c=='R':result-=1
            else: _+=1
        return abs(result)+_