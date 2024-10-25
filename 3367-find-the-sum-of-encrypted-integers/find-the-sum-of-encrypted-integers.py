class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans=0
        
        def encryptedNum(num):
            return int(sorted(str(num))[-1]*len(str(num)))
        for i in nums:
            ans+=encryptedNum(i)

        return ans
            
        