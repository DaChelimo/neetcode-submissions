class Solution:
    # Create a set
    # Compare the length of the set and the array
    # If equal, distinct. Else, duplicates
    # Time: O(n). Space: O(n)
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     distinct = set(nums)
    #     return len(distinct) != len(nums)

    # or
    
    # Create set
    # Iterate through nums, check the set for elem and return True if present.
    # IF absent, add elem to set
    # Return False
    # Edge Cases: nums empty -> False

    # Space: O(n). Time: O(n)

    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for elem in nums:
            if elem in seen:
                return True
            seen.add(elem)
        
        return False