class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ~ case insensitive - convert to lowercase
        char_arr = []

        for char in s:
            if char.isalnum() == True:
                char_arr.append(char.lower())

        l = 0
        r = len(char_arr) - 1

        while l < r:
            if char_arr[l] != char_arr[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
        