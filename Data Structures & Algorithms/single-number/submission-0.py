class Solution:
    # Create a result
    # Loop through single number and XOR with result
    # XOR is associative hence a ^ b ^ c ^ a ^ c = b
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result = result ^ num
        
        return result

        