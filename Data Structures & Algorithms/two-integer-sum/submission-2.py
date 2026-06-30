class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for index, value in enumerate(nums):
            num_to_find = target - value

            if num_to_find in nums_dict:
                return [nums_dict[num_to_find], index]
            else:
                nums_dict[value] = index

        


        