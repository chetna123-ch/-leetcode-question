from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        # First pass: find candidate
        for x in nums:
            if count == 0:
                candidate = x
                count = 1
            elif x == candidate:
                count += 1
            else:
                count -= 1

        # Second pass: verify candidate (optional if majority is guaranteed)
        count_candidate = 0
        for x in nums:
            if x == candidate:
                count_candidate += 1

        if count_candidate > len(nums) // 2:
            return candidate

        return -1  # or raise an exception if you prefer