class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(0, len(nums)):
            index_to_negate = abs(nums[i]) - 1
            if nums[index_to_negate] > 0:
                nums[index_to_negate] *= -1
            else:
                return abs(nums[i])
