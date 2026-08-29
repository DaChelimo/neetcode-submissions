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
        
        def dfs(i, curr, total):
            if total == target:
                results.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            # Include the number
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)

        return results


        

        