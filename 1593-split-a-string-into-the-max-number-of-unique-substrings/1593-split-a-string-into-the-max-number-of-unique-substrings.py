class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        substrings = set()
        def backtrack( s, start, substrings):
            if start == len(s):
                return 0

            max_count = 0

            for end in range(start + 1, len(s) + 1):
                sub_string = s[start:end]
                if sub_string not in substrings:
                    substrings.add(sub_string)
                    max_count = max(max_count, 1 + backtrack(s, end, substrings))
                    substrings.remove(sub_string)

            return max_count
        return backtrack(s, 0, substrings)

    