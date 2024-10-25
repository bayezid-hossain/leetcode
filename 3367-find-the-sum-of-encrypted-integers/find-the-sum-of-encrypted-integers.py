class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans=0
        
        def encryptedNum(num):
            maxval = 0
            count=0
            while num>0:
                maxval=max(maxval,num%10)
                num//=10
                count+=1
            return int(str(maxval)*count)
        for i in nums:
            ans+=encryptedNum(i)

        return ans
            
        