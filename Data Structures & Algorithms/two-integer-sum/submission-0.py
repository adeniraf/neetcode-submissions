class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = {}

        for index, value in enumerate(nums):
            to_find = target - value

            if to_find not in nums_dict:
                nums_dict[value] = index
            else:
                return [nums_dict[to_find], index]
            
        