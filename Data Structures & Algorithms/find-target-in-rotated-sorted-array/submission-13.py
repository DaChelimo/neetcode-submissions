class Solution:

    # While left <= right
    # If target = mid, return target
    # If left half is sorted:
    #   If target > left and target < mid, move left. 
    #       else, move right
    # Else (left half not sorted)
    #   If target > mid and target < right, move right
    #       else, move left
    
    # Loop terminates means absence. Return -1
    # Time: O(lg n). Space: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

        