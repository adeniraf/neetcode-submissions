class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # add num and freq to dictionary
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1

        index_freq_array = [[] for i in range(len(nums)+1)]
        for num, freq in nums_dict.items():
            index_freq_array[freq].append(num)
        
        output_arr = []

        for arr in reversed(index_freq_array):
            print(arr)
            while len(arr) > 0:
                if len(output_arr) == k:
                    return output_arr
                else:
                    output_arr.append(arr.pop())
        return output_arr



