class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        for a,b in zip(word1,word2):
            result+=a+b
        if len(word1)>len(word2):
            result+=word1[len(word2):]
        elif len(word2)>len(word1):
            result+=word2[len(word1):]
       
        return result