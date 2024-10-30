class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        if n<3:
            return False
        increasing=True
        for i in range(n-1):
            if increasing:
                if arr[i]>=arr[i+1]:
                    increasing=False
                    if i==0:
                        return False
            elif not increasing:
                if arr[i]<=arr[i+1]:
                    return False

        return True if arr[-1]<arr[-2] else False
