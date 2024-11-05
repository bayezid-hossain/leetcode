class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counter=Counter(moves)
        max_value=abs(counter['L']-counter['R'])
        return max_value+counter["_"]