class Solution:
    # // PLAN:
    # // 1a. Create left and right indices
    # // 1. Check the middle, compare it with the target ([while] looping with the index, number)
    # // 2. If middle == target, return the index;
    # //       middle > target, move right = middle - 1
    # //       middle < target, move left = left + 1
    # // 3. If left > right, return -1  

    # // Time: O(log n). Space: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while (left <= right):
            middle_index = (left + right) // 2
            middle = nums[middle_index]

            if middle == target:
                return middle_index
            elif middle > target:
                right = middle_index - 1
            else:
                left = middle_index + 1
        
        return -1