class Solution:
    # Create l, r, mid
    # Create result
    # If nums is sorted, compare result and nums[l], break
    # If nums[mid] in left sorted list, check right (move l = mid + 1)
    # If nums[mid] in right sorted list, check left (move r = mid - 1)
    # Return result
     def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                result = min(result, nums[l])
                break;
            
            mid = (l + r) // 2

            if nums[mid] >= nums[l]: # 3, 4, 5, 1, 2
                l = mid + 1
            else:
                result = min(result, nums[mid])
                r = mid - 1

        return result



            

    
        