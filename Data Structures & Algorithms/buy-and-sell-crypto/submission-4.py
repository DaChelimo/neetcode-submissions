class Solution:
    # 1. Create left and right, max 
    # 1, 2, 3, 4, 5
    # 5, 4, 3, 2, 1
    # 5, 1, 2, 6, 3
    # 2. Compare diff with max. If diff positive, we advance right
    #  3. If diff is negative, left = right, move right = right + 1
    #  4 Return max
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max = 0

        while r < len(prices):
            diff = prices[r] - prices[l]

            if diff > max:
                max = diff
            elif diff < 0:
                l = r
                r = r + 1
            else:
                r += 1
        
        return max 
        