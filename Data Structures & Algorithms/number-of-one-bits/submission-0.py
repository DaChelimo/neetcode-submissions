class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n > 0:
            if (n & 0b1):
                res += 1
            n >>= 1 
            # We can do this since n is unsigned hence right shift is logical (adds 0 in MSB)
        
        return res
        