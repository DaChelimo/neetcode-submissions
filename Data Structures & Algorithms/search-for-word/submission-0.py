class Solution:

    # RECURSION
    # Create target -> represents the char we are looking for ["CAT" -> C - 1, A - 2..]
    # Define dfs(r, c, target)
    # Don't: r < 0 or > ROWS. c < 0 > COLUMNS. target > len(word)
    # Do: If target == char, return true
    # found = dfs(on all four directions)
    # Create visited => add to visited inside dfs, explore all directions, 
    #                   if not found, remove position from visited
    # Visited.add((r, c))

    # 

    # CONSTRAINTS: 
    # 1. Directions: up, down, left, right
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS = len(board)
        COLUMNS = len(board[0])

        def dfs(r, c, target):
            if target == len(word): # All letters found
                return True

            if ((r < 0 or r >= ROWS) or 
                (c < 0 or c >= COLUMNS) or 
                (r, c) in visited or
                board[r][c] != word[target]
            ): 
                return False
            
            visited.add((r, c))

            found = (dfs(r + 1, c, target + 1) or 
                    dfs(r - 1, c, target + 1) or
                    dfs(r, c + 1, target + 1) or
                    dfs(r, c - 1, target + 1))
            
            visited.remove((r, c))

            return found
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(r, c, 0):
                    return True
        
        return False
            