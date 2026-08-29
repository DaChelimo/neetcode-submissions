class Solution:
    # RECURSION
    # Create results -> permanent
    # Create path -> temporary and edited by every travesal

    # DFS (i, total): // exploration
        # if total == target: add to results
        # if total > target: return
        # 
        # path.append(num)
        # dfs(i)
        # path.pop()

    # In a for loop, Explore all possible paths (using dfs)

    # Time: O(n^2). Space: O(n)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        path = []

        def dfs(start, total):
            if total == target:
                results.append(path.copy())
                return
            
            if total > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, total + nums[i])
                path.pop()
        
        dfs(0, 0)
        return results

        

        