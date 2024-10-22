class Solution:
    def reverseWords(self, s: str) -> str:
        splited_words=s.split()
        result=[]
        for i in range(len(splited_words)-1,-1,-1):
            result.append(splited_words[i])
        
        return " ".join(result)