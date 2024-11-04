class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if abs(arr[i]-arr[j])>a:
                    continue
                for k in range(j+1,len(arr)):
                    if abs(arr[j]-arr[k])>b or abs(arr[i]-arr[k])>c:
                        continue
                    else:
                        count+=1
        return count
                    