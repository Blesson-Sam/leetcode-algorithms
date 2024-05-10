class Solution:
    def rob(self, nums: list[int]) -> int:
        a = b = 0
        for i in nums:
            a, b = max(a, b), a + i
        
        return max(a, b)