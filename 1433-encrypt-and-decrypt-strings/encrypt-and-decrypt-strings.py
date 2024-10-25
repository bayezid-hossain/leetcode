class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        
        self.hashmap=dict()
        for i in range(len(keys)):
            self.hashmap[keys[i]]=values[i]
        self.dictmap=defaultdict(int)
        for word in dictionary:
            self.dictmap[self.encrypt(word)]+=1

   
    def encrypt(self, word1: str) -> str:
        result=""
        
        for c in word1:
            if c in self.hashmap:
                result+=self.hashmap[c]
            else:
                return ""
        return result
            

    def decrypt(self, word2: str) -> int:
        return self.dictmap[word2]
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)