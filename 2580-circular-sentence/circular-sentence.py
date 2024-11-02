class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words=sentence.split()
        
        last_char=words[0][-1]
        
        for i in range(1,len(words)):
            if last_char!=words[i][0]:
                return False
            else:
                last_char=words[i][-1]
        
        return last_char==words[0][0]