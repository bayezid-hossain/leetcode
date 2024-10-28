class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        def update(i, x):
            i += n
            while i:
                tree[i] = max(tree[i], x)
                i //= 2
            
        def query(i, j):
            i += n
            j += n
            ans = -inf
            while i <= j:
                if i & 1:
                    ans = max(ans, tree[i])
                    i += 1
                if not j & 1:
                    ans = max(ans, tree[j])
                    j -= 1
                i //= 2
                j //= 2
            return ans
        
        ma = max(nums)
        n = ma + 1
        tree = [0] * (2 * n)
        ans = 0
        
        for i, v in enumerate(nums):
            # right query boundary
            rq = max(0, v - 1)
            # left query boundary
            lq = max(0, v - k)
            # query
            res = query(lq, rq) + 1
            # update LIS length for current value
            ans = max(ans, res)
            if res > tree[v + n]:
                update(v, res)

        return ans