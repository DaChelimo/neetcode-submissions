class Solution:
    # Recursion

    # n = 3 -> [1, 2, 3]
    # Create results 

    # Create an inner function: dfs(i, curr, total)
    # if total > target, return 
    # if total == target, add to results, and return

    # for i in range(start, end of list), curr.append(nums[i]) dfs(i) curr.pop(nums[i])
    # return len(results)

    # Time: O(n ^ 2). Space: O(n ^ n)
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(total):
            if total == n:
                return 1
            elif total > n:
                return 0
            
            if total in memo:
                return memo[total]
            
            memo[total] = dfs(total + 1) + dfs(total + 2)
            return memo[total]
        
        return dfs(0)