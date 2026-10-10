from collections import deque

class Solution:
    # 1. Get num of rows and columns and create islands
    # 2. Create visited (set containing visited nodes (r, c))
    # 3. Loop through rows and columns
    # 4. In iteration[r][c], check if that node: 
    #       a. has not been seen already
    #       b. is 1
    # 5. If so, do bfs on it, and add 1 to the islands

    # Bfs structure:
    # 1. Create a list of directions, and a deque of nodes to visit
    # 2. If a node is 1 and not seen, add its neighbours to the deque
    # 3. stop when the nodes to visit are over

    # Time: O(m * n); Space: O(m * n)
    # Constraints: grid is none, return 0
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 

        def bfs(r, c):
            # Move: down, up, right, left
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            
            while queue:
                (r, c) = queue.popleft()

                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc

                    if 0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in visited and grid[newR][newC] == "1":
                        queue.append((newR, newC))
                        visited.add((newR, newC))
            
            

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands
                    

        
        