# 977) Squares of a Sorted Array.
class Solution:
    def sortedSquares(self, nums) -> list[int]:
        return sorted([i*i for i in nums])
