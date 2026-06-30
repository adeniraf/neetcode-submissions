class Solution:
    def isPalindrome(self, s: str) -> bool:

        # case insensitive
        #  ignores non-alphanumeric characters
        alpha_num_array = []
        # copy the string into a new string, removing non alpha-numeric characters
        for char in s:
            if char.isalnum() == True:
                alpha_num_array.append(char.lower())

        print(alpha_num_array)


        # put two pointers: one at start, one at the end and compare all the characters
        i, j = 0, len(alpha_num_array) - 1

        while i < j:
            if alpha_num_array[i] != alpha_num_array[j]:
                return False
            else:
                i += 1
                j -= 1

        return True



        