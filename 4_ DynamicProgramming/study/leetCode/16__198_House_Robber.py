# 198. House Robber
# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        prev_2 = nums[0]
        prev_1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(prev_1, prev_2 + nums[i])
            prev_2 = prev_1
            prev_1 = curr

        return prev_1
