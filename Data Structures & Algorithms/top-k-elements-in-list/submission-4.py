class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # add num and freq to dictionary
        nums_dict = {}
        for i in range(0, len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1

        dict_values = list(nums_dict.items())

        # sorting num-freq pairs by the frequency
        dict_values.sort(key=lambda pair: -pair[1])

        i, output_arr = 0, []
        while i < k:
            num_to_append = dict_values[i][0]
            output_arr.append(num_to_append)
            i += 1

        return output_arr
