class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        dir=[[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        target="123450"
        visited=set()
        q=deque()
        start=""

        for row in board:
            for col in row:
                start+=str(col)
        
        q.append(start)
        visited.add(start)
        step=0

        while q:
            size=len(q)

            for _ in range(size):
                current=q.popleft()

                if current==target:
                    return step
                zero=current.find("0")

                for move in dir[zero]:
                    next_state=list(current)
                    next_state[zero],next_state[move]=next_state[move],next_state[zero]
                    next_state="".join(next_state)
                    if next_state not in visited:
                        visited.add(next_state)
                        q.append(next_state)
            step+=1
        return -1

#         Problem Understanding:

# You are given a sliding puzzle with a 2x3 grid. The goal is to arrange the grid in the target configuration "123450", where the 0 represents the empty space that can be moved up, down, left, or right.
# Approach:

# We use Breadth-First Search (BFS), where each state of the board is represented as a string. BFS ensures we find the shortest path to the target configuration.
# Steps:

# Convert the 2D board into a string for easier manipulation.
# Use BFS to explore all possible moves. At each state, try to swap the 0 with its adjacent cells.
# Track visited configurations to avoid revisiting states.
# Once the target is found, return the number of steps taken.
# Complexity Analysis:
# Time Complexity:

# O(N), where N is the number of possible states (i.e., the number of permutations of the board configuration). In this case, there are at most 720 states for a 2x3 puzzle.
# Space Complexity:

# O(N), where N is the number of states stored in the queue and the visited set. We store all possible states during the BFS.