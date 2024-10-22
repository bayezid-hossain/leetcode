class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        start=1
        if len(flowerbed)<2:
            if flowerbed[0]==0:
                n-=1
            return True if n<=0 else False
            
        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            n-=1
            start=2
        for i in range(start,len(flowerbed)-1):
            if n==0:
                return True
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                # print(i)
                n-=1
                flowerbed[i]=1
                i+=2
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            n-=1
        return True if n<=0 else False