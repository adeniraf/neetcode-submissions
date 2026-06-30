class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = set()
        for num in nums:
            if num not in output:
                output.add(num)
            else:
                return True
        
        return False
        