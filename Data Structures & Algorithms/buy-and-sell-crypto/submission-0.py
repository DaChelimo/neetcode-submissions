class Solution:
    # INPUT: list of prices
    # OUTPUT: Int  -> max profit [max(0, profit)]

    # Constraints: Decreasing list -> 10, 8, 2 -> Profit: 0

    # PLAN
    # 1. Create profit = 0
    # 2. Loop from 0..len(list), checking i vs the nums following it
    # 3. If num - i > profit, update profit
    # 4. REturn profit, 0
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            curr = i + 1
            while (curr < len(prices)):
                margin = prices[curr] - prices[i]

                if (margin > profit):
                    profit = margin

                curr += 1
            
        return profit
        