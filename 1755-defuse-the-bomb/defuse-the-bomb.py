class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        temp=[0]*len(code)
        if k==0:
            return temp
        elif k>0:
            for i in range(len(temp)):
                start=(i+1+abs(k))-len(temp)
                temp[i]=sum(code[i+1:i+1+abs(k)])
                if start>0:
                    temp[i]+=sum(code[0:start])
        elif k<0:
            for i in range(len(temp)):
                end=len(temp)+(i-abs(k))
                temp[i]=sum(code[max(0, i+k):i])
                if end>0:
                    temp[i]+=sum(code[end:])
        return temp