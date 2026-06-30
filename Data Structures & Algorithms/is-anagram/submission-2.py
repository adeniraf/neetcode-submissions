class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char_dict = {}

        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

        print(char_dict)
        
        for char in t:
            if char not in char_dict:
                return False
            
            if char_dict[char] > 1:
                char_dict[char] -= 1
            else:
                del char_dict[char]

        if len(char_dict) > 0:
            return False

        return True