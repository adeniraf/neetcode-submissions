class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # add num and freq to dictionary
        nums_dict = {}

        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        print(nums_dict)

        # create an array with length of nums+1 and store each number at the index that
        # corresponds to its frequency
        num_freq_array = [[] for i in range(len(nums)+1)]

        for num, freq in nums_dict.items():
            num_freq_array[freq].append(num)
        print(num_freq_array)

        output_arr = []
        for i in range(len(num_freq_array)-1, 0, -1):  
            for num in num_freq_array[i]:
                output_arr.append(num)
                if len(output_arr) == k:
                    return output_arr
