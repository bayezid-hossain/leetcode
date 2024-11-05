class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        counter=Counter(moves)
        return True if counter["U"]==counter["D"] and counter["L"]==counter["R"] else False
            