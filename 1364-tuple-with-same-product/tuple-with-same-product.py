class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashmap={}

        result=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                res=nums[i]*nums[j]
                if res in hashmap:
                    hashmap[res]+=1
                    
                else:
                    hashmap[res]=1
        #print(hashmap)
        for product_frequency in hashmap.values():
            # Calculate the number of ways to choose two pairs with the same product
            pairs_of_equal_product = (
                (product_frequency - 1) * product_frequency // 2
            )

            # Add the number of tuples for this product to the total (each pair
            # can form 8 tuples)
            result += 8 * pairs_of_equal_product

        return result
        
