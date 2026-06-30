class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0

        for num in nums:
            seen.add(num)

            if num - 1 not in seen:
                current = 1
                while num + 1 in seen:
                    current += 1
                    num += 1
                longest = max(longest, current)
            else:
                while num - 1 in seen:
                    num -= 1
                current = 1
                while num + 1 in seen:
                    current += 1
                    num += 1
                longest = max(longest, current)
        
        return longest

                