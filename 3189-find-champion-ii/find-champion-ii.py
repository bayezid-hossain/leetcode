class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        possible_winner=[True]*n

        for a,b in edges:
            possible_winner[b]=False
        winner=-1
        winner_count=0

        for i in range(0,n):
            if possible_winner[i]:
                winner=i
                winner_count+=1
        
        if winner_count==1:
            return winner
        return -1
        