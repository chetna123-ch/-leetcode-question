from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        r = 0
        l = 0

        while r < n:   # fix loop condition
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1

        return l   # return new length
