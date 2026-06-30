class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the two strings and compare
        # sorting - O(log n) time complexity
        # inserting into the dictionary - O(1) T.C
        # comparing the two dicts - O(n)
        # Space complexity - O(2n)

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s != sorted_t:
            return False
        return True

        