class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strNums=[]
        for i in nums:
            strNums.append(str(i))
        result=""
        def compare(a, b):
            if b + a > a + b:
                return 1
            elif b + a < a + b:
                return -1
            else:
                return 0

        for string in sorted(strNums,key=cmp_to_key(compare)):
            result+=string
        return result if result[0]!="0" else "0"