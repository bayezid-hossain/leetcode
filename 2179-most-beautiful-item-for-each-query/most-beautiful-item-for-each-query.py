class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        #bruteforce
#         result=[]
#         for query in queries:
#             max_beauty=0
#             for i in items:
#                 if i[0]<=query:
#                     max_beauty=max(max_beauty,i[1])
            
#             result.append(max_beauty)
#         # print(result)
#         return result

        #optimal than bruteforce
        # print(queries)
       
        maxI=float('inf')
        res=[[0,0,maxI]]
        items.sort(key=lambda x:x[0])
        for price,beauty in items:
            lastBracket=res[-1]
            if beauty>lastBracket[1]:
                res[-1][2]=price
                res.append([price,beauty,maxI])
        ans=[]
        for query in queries:
            for i in range(len(res)-1,-1,-1):
                if res[i][0]<=query:
                    ans.append(res[i][1])
                    break
        return ans