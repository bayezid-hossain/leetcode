class Solution:
    def compressedString(self, word: str) -> str:
        if len(word)<1:
            return ""
        last_char=word[0]
        last_count=0
        result=""
        def ninedivisible(char,count):
            return (f"9{char}"*(count//9))+(f"{count%9}{char}" if count%9>0 else "")
        for c in word:
            if last_char==c:
                last_count+=1
            else:
                result+=ninedivisible(last_char,last_count)
                last_char=c
                last_count=1
        
        result+=ninedivisible(last_char,last_count)
        return result
        # print(result)
