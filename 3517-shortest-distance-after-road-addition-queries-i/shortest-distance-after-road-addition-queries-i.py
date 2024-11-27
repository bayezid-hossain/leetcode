class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        roadmap={}
        result=[]
        for i in range(n):
            roadmap[i]=[i+1]
        
        def bfs(graph):
            nonlocal result
            # Queue to store the nodes in the order they are visited
            q = deque()
            dist=[float('inf')]*n
            # Mark the distance of the source node as 0
            dist[0] = 0
            # Push the source node to the queue
            q.append(0)

            # Iterate until the queue is not empty
            while q:
                # Pop the node at the front of the queue
                node = q.popleft()

                # Explore all the neighbors of the current node
                for neighbor in graph[node]:
                    # Check if the neighboring node is not visited
                    if neighbor<n and dist[neighbor] == float('inf'):
                        # Mark the current node as the parent of the neighboring node
                        # Mark the distance of the neighboring node as the distance of the current node + 1
                        dist[neighbor] = dist[node] + 1
                        # Insert the neighboring node to the queue
                        q.append(neighbor)
            result.append(dist[-1])
        for a,b in queries:
            roadmap[a].append(b)
            bfs(roadmap)
        return result