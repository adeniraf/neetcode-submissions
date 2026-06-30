class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        minVal = nums[0]

        while low <= high:
            mid = (low + high) // 2

            if nums[high] > nums[low]:
                minVal = min(minVal, nums[low])
                return minVal

            else:
                if nums[mid] >= nums[low]:
                    minVal = min(minVal, nums[low])
                    low = mid + 1

                else:
                    minVal = min(minVal, nums[mid])
                    high = mid - 1
        return minVal