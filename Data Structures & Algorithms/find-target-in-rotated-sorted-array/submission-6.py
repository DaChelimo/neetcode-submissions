class Solution:
    # Binary search
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            
            # In Left Sorted Array
            if nums[l] <= nums[mid]:
                if target > nums[mid]:
                    l = mid + 1
                else:
                    if target >= nums[l]:
                        r = mid - 1
                    else:
                        l = mid + 1
            else:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    if target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1

        return -1


        