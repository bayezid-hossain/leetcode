class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap=set()
        
        for i in arr:
            if i*2 in hashmap or (i%2==0 and i//2 in hashmap):
                return True
            hashmap.add(i)
        return False
            
        