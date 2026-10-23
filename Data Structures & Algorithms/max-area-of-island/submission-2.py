from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        # Loop through every row and col
        # Do bfs on every eligible node, and store area (comparing with max once queue is empty)

        rows = len(grid)
        cols = len(grid[0])
        seen = set()

        def bfs(i: int, j: int) -> int:
            queue = deque([(i, j)])
            seen.add((i, j))
            size = 0

            directions = [(0, - 1), (0, 1), (-1, 0), (1, 0)]

            while queue:
                curr_i, curr_j = queue.popleft()
                size += 1
                
                for (delta_i, delta_j) in directions:
                    new_i = curr_i + delta_i
                    new_j = curr_j + delta_j

                    if 0 <= new_i < rows and 0 <= new_j < cols and (new_i, new_j) not in seen and grid[new_i][new_j] == 1:
                        queue.append((new_i, new_j))
                        seen.add((new_i, new_j))
                        
            
            return size


        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen and grid[i][j] == 1:
                    maxArea = max(bfs(i, j), maxArea)
        
        return maxArea