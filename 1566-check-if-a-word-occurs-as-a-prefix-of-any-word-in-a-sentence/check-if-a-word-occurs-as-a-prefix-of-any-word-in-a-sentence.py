class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr=sentence.split(" ")
        count=1
        for word in arr:
            if word.startswith(searchWord):
                return count
            count+=1
        return -1