class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        output_arr = [[] for i in range(len(nums) + 1)]

        nums_dict = {}

        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        dict_arr = nums_dict.items()
        
        for num, count in dict_arr:
            output_arr[count].append(num)

        final_output = []
        
        for i in range(len(output_arr) - 1, 0, -1):
            if len(output_arr[i]) == 0:
                continue
            
            while len(output_arr[i]) != 0:
                if len(final_output) != k:
                    final_output.append(output_arr[i].pop())
                else:
                    return final_output

        return final_output