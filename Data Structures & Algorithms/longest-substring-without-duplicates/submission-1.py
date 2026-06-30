class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        hashmap = set()

        max_substr = 0
        while j < len(s):
            if s[j] not in hashmap:
                hashmap.add(s[j])
                max_substr = max(max_substr, len(hashmap))
                j += 1
            else:
                while s[j] in hashmap:
                    hashmap.remove(s[i])
                    i +=1
        return max_substr