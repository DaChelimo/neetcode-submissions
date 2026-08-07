class Solution:

    # Input: arr nums, int target
    # Output: indices i, j

    # Constraints: smaller index first. 
    # Promises: i & j exist and distinct

    # Create a hashmap called seen (key -> num, value -> index)
    # Loop through nums, check if target - num in seen
    # If true, get value (index). Return index 1, index 2 (current)

    # Time: O(n). Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for index, value in enumerate(nums):
            if (target - value) in seen:
                firstIndex = seen[target - value]
                return [firstIndex, index]
            
            seen[value] = index

        return []
        