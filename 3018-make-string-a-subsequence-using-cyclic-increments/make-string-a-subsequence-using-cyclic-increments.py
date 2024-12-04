class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        hashmap = {
    'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
    'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
    'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'
}
        length1=len(str1)
        length2=len(str2)
        if length2>length1:
            return False
        pointerSub=0
        pointerMain=0
        while pointerMain<length1 and pointerSub<length2:
            cur_main=str1[pointerMain]
            next_sub=str2[pointerSub]
            if cur_main==next_sub or hashmap[cur_main]==next_sub:
                pointerSub+=1
            pointerMain+=1
        return True if pointerSub==length2 else False

            
