class Solution:
    # INPUT: list of prices
    # OUTPUT: Int  -> max profit [max(0, profit)]

    # Constraints: Decreasing list -> 10, 8, 2 -> Profit: 0
                #  Empty list -> 0

    # PLAN
    # 1. Create two pointers (l = 0 and r = 1), and max_p
    # 2. Keep l at the lowest we find
    # 3. Loop through array (r), we check if (prices[r] < prices[l]) => l = r, r = r + 1
    # 4. Else, get profit = p[r] - p[l], compare max_p, update accordingly
    # return max_p

    # Time: O(n). Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if len(prices) < 2:
            return 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                curr_profit = prices[r] - prices[l]
                max_profit = max(curr_profit, max_profit)
            
            r += 1    
        
        return max_profit
        