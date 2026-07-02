class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {}

        for strx in strs:
            sorted_string = "".join(sorted(strx))
            if sorted_string not in anagram_dict:
                anagram_dict[sorted_string] = [strx]
            else:
                anagram_dict[sorted_string].append(strx)

        output_arr = []

        for value in anagram_dict.values():
            output_arr.append(value)

        return output_arr