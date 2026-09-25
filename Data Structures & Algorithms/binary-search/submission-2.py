class Solution:
    # 1. Use binary search
    # 2. Create left and right pointers
    # 3. Get the middle, and compare with the value at nums[middle]
    # 4a. If value == num[middle], return middle
    # 4. If value > nums[middle], make left = middle + 1
    # 4c. else, make right = middle - 1

    # Time: O(lg n). Space: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1
        
    
        