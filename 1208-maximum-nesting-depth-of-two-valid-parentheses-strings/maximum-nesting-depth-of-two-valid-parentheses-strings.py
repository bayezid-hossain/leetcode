class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        A=0
        B=1

        depth=[0,0]
        res=[]
        for c in seq:

            if c=='(':
                
                next=A if depth[A]<=depth[B] else B
                res.append(next)
                depth[next]+=1
            else:
                next=A if depth[A]>=depth[B] else B
                res.append(next)
                depth[next]-=1
        return res