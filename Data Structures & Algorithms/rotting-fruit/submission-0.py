from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])

        totalFruits = 0
        totalRotten = 0

        queue = deque([])

        for i in range(rows):
            for j in range(cols):
                cell = grid[i][j]

                totalFruits += 1 if (cell != 0) else 0
                if cell == 2:
                    queue.append((i, j))
                    seen.add((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        level = 0

        # Load all the initial rotten oranges, and then do BFS on all of them and add to queue. Repeat until queue is empty.
        # If rotten == allFruits, valid.. else, return False
        # Levels represents minutes

        while queue:
            for _ in range(len(queue)):
                curr_i, curr_j = queue.popleft()
                totalRotten += 1

                for delta_i, delta_j in directions:
                    ni, nj = curr_i + delta_i, curr_j + delta_j

                    if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in seen and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
                        seen.add((ni, nj))
            
            if queue:
                level += 1
                    
        return level if totalRotten == totalFruits else -1
