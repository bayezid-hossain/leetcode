class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hashmap={}

        row=len(matrix)
        col=len(matrix[0])
        for i in range(row):
            string=""
            if matrix[i][0]==0:
                for j in range(col):
                    string+=str(matrix[i][j])

            else:
                for j in range(col):
                    if matrix[i][j]==0:
                        string+='1'
                    else:
                        string+='0'
            # print(string)
            if string not in hashmap:
                hashmap[string]=1
            else:
                hashmap[string]+=1
        return (max(hashmap.values()))

                
