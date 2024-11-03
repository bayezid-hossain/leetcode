class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        # instead of removing from both the ends 
        # you can you technique to get the longest substring to get the characters count(char) - k
        # if any character count goes below 0 then return -1

        # for all the character count decrease by k
        limit = {char: s.count(char) - k for char in "abc"}
        print("Limit:",limit)
        if any(x < 0 for x in limit.values()):
            return -1
        
        cnts = {c: 0 for c in 'abc'}
        print("Counts:",cnts)
        ans = l = 0
        for r, c in enumerate(s):
            cnts[c] += 1

            while cnts[c] > limit[c]:
                cnts[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return len(s) - ans

