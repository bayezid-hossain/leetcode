class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies=max(candies)
        result=[False]*len(candies)
        
        for i in range(len(candies)):
            result[i]=True if extraCandies+candies[i] >= max_candies else False
            
        return result