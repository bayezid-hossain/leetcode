class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        if start==target:
            return True
        waitLeftCounter=0
        waitRightCounter=0

        for curr,goal in zip(start,target):
            if curr=="R":
                if waitLeftCounter>0:
                    return False
                waitRightCounter+=1
            if goal=="L":
                if waitRightCounter>0:
                    return False
                waitLeftCounter+=1
            if goal=="R":
                if waitRightCounter==0:
                    return False
                waitRightCounter-=1
            if curr=="L":
                if waitLeftCounter==0:
                    return False
                waitLeftCounter-=1
        return waitLeftCounter==0 and waitRightCounter==0
        
  
