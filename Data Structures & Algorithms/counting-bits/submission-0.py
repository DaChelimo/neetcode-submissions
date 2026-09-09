class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 -> 0000
        # 1 -> 0001

        # 2 -> 0010
        # 3 -> 0011

        # 4 -> 0100
        # 5 -> 0101
        # 6 -> 0110
        # 7 -> 0111

        # 8 -> 1000
        # 11 -> 1011

        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[i - offset]

        return dp

