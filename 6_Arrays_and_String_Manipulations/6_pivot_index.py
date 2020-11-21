# 724

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        lsum = 0
        
        for i, current in enumerate(nums):
            rsum = s - (lsum + current)
            
            if lsum == rsum:
                return i
            
            lsum += current
            
        return -1

