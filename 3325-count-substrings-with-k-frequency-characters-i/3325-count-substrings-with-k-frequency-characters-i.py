class Solution:
    def numberOfSubstrings(self,s, k):

        ans = 0

        for i in range(len(s)):
            freqArr = [0] * 26

            for j in range(i, len(s)):
                freqArr[ord(s[j]) - ord('a')] += 1
                
                if freqArr[ord(s[j]) - ord('a')] == k:
                    ans += len(s) - j
                    break
        
        return ans
            