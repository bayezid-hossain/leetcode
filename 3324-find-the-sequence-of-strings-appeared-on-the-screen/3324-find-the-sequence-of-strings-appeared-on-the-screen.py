class Solution:
    def stringSequence(self, target: str) -> List[str]:
        subs=["a"]
        string=["a"]
        index=0
        while True:
            while string[index]!=target[index]:
                string[index]=chr(ord(string[index])+1)
                subs.append(''.join(string))
            index+=1
            if len(string)==len(target):
                break
            else:
                subs.append(''.join(string)+"a")
                string.append("a")
        return subs
            