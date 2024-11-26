class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n==1 and len(edges)==0:
            return 0
        champ_map=set({})
        disqualified_map=set({})
        for edge in edges:
            if edge[0] not in disqualified_map:
                champ_map.add(edge[0])
            
            if edge[1] in champ_map:
                champ_map.remove(edge[1])
            disqualified_map.add(edge[1])
        if len(champ_map)+len(disqualified_map)!=n or len(champ_map)!=1:
            return -1
        return champ_map.pop()
        