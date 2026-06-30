class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output_dict = {}
        
        for i in range(0, len(nums)):
            curr_num = nums[i]
            num_to_find = target - curr_num

            if num_to_find not in output_dict:
                output_dict[curr_num] = i
            else:
                return [output_dict[num_to_find], i]
