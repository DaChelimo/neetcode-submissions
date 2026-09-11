class Solution:
    # Find leading bit position (shift right (logical - 0) and &0b1)
    # Left shift by 32 - position

    # Time: O(n). Space: O(1)
    def reverseBits(self, n: int) -> int:
        msb_position = 0
        result = 0
        
        # 0011 -> index 0 -> index 3, i 1 -> i 2
        for i in range(32):
            if (n >> i & 0b1):
                msb_position = i
                new_bit = 1 << 32 - (i + 1)
                result += new_bit
        
        # shift_by = 32 - msb_position - 1
        return result
        
        