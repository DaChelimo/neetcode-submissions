class Solution:
    # Create a set
    # Compare the length of the set and the array
    # If equal, distinct. Else, duplicates
    # Time: O(n). Space: O(n)
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct = set(nums)
        return len(distinct) != len(nums)