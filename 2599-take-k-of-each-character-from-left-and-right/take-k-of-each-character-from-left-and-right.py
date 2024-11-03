class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # make a duplicate and count
        ss = s*2
        freq = {'a': s.count('a'), 'b': s.count('b'), 'c': s.count('c')}

        if any([v < k for v in freq.values()]): # using any() to check if impossible
            return -1

        # just some variables
        windows = []
        start = 0
        end = len(s)-1

        # make sure start never crosses the boundary
        while start < len(s):

            # as long as the window is still valid and start doesn't cross the boundary
            while start < len(s) and all([v >= k for v in freq.values()]):
                # get rid of previous letter
                freq[s[start]] -= 1
                # next!
                start += 1

            windows.append(end-start+2)

            # as long as the window isn't valid
            while end < len(ss)-1 and any([v < k for v in freq.values()]):
                end += 1
                freq[ss[end]] += 1
            windows.append(end-start+1)

        # just return the smallest window size
        return min(windows)