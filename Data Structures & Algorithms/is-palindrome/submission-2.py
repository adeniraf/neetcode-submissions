class Solution:
    def isPalindrome(self, s: str) -> bool:
        output_arr = []
        for char in s:
            if char.isalnum():
                output_arr.append(char.lower())

        i, j = 0, len(output_arr) - 1

        while i <= j:
            if output_arr[i] != output_arr[j]:
                return False
            i += 1
            j -= 1
        return True
        
