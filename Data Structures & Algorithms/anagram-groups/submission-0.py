class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        str_dict = {}

        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in str_dict:
                str_dict[sorted_str] = [str]
            else:
                str_dict[sorted_str].append(str)
        print(str_dict)
        output_arr = []
        for str_arr in str_dict.values():
            output_arr.append(str_arr)

        return output_arr