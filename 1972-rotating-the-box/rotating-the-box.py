class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        row=len(box)
        col=len(box[0])
        queue=[]
        for r in range(row):
            for c in range(col-1,-1,-1):
                if box[r][c]==".":
                    queue.append(c)
                elif box[r][c]=="*":
                    queue=[]
                else:
                    box[r][c]="."
                    queue.append(c)
                    box[r][queue.pop(0)]="#"
                    
            queue=[]
        result=[]

        for c in range(col):
            temp=[]
            for r in range(row-1,-1,-1):
                
                temp.append(box[r][c])
            result.append(temp)
        return result