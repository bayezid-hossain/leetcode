class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        A=0
        B=1

        depth=[0,0]
        res=[]
        for c in seq:

            if c=='(':
                next=0
                if depth[A]<=depth[B]:
                    next=A
                else:
                    next=B
                res.append(next)
                depth[next]+=1
            else:
                next=0
                if depth[A]>=depth[B]:
                    next=A
                else:
                    next=B
                res.append(next)
                depth[next]-=1
        return res