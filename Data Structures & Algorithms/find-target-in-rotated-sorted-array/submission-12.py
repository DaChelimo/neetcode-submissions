class Solution:
    # Create left and right pointers. 
    # Get middle. Check if middle == targer, and return index if target
    # Check what side it is on. 
    # If target = 4 and middle = 5, check if target is greater than right and less than middle. If so, move left

    # [3,4,5,6,1,2]
    # Otherwise, move right
    # If greater than left and less than middle, means it is in the left side, move left = middle + 1

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

        