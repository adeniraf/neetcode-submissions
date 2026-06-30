class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add all values and their indexes to a hashmap
        nums_dict = {}

        for i, v in enumerate(nums):
            nums_dict[v] = i

        max_substr = 0
        # loop over the array once
        for num in nums:
            curr_max_substr = 1
            # if current_value - 1 is in the hashmap, then, while curr_value - 1 is in hashmap, decrement the value
            if num - 1 in nums_dict:
                while num - 1 in nums_dict:
                    num -= 1

            # if the current_value - 1 is not in the hashmap, then it's the start of a current substring
            while num + 1 in nums_dict:
                curr_max_substr += 1
                num += 1

            max_substr = max(max_substr, curr_max_substr)

        return max_substr



        

        # while current value + 1 in hashmap, store the length of the current substring