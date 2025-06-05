# LeetCode Question: 169
# The below program is to return the majority element from the given list ( more than length(list)/2 )

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        length = len(nums)
        return nums[length//2]
    