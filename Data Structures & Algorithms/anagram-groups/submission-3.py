class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {}

        for str in strs:
            sorted_str = "".join(sorted(str))

            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = [str]
            else:
                anagram_dict[sorted_str].append(str)

        output_arr = []
        for value in anagram_dict.values():
            output_arr.append(value)

        return output_arr
        