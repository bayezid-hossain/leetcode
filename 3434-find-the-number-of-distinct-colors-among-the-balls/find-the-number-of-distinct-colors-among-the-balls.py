class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colormap={}
        res=[]
        indexmap={}
        for index,color in queries:
            if not color:
                res.append(len(colormap))
                continue
            if color not in colormap and index not in indexmap:
                colormap[color]={index}
                indexmap[index]=color
            elif color not in colormap and index in indexmap:
                oldcolor=indexmap[index]
                indexmap[index]=color
                colormap[oldcolor].remove(index)
                if len(colormap[oldcolor])==0:
                    colormap.pop(oldcolor)
                colormap[color]={index}
            elif color in colormap and index in indexmap:
                oldcolor = indexmap[index]
                colormap[oldcolor].remove(index)
                indexmap[index]=color
                if len(colormap[oldcolor])==0:
                    colormap.pop(oldcolor)
                if color not in colormap:
                    colormap[color]={index}
                else:
                    colormap[color].add(index)
            elif color in colormap and index not in indexmap:
                indexmap[index]=color
                colormap[color].add(index)
            res.append(len(colormap))
        return res