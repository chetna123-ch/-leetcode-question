class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        left =0
        win_sum = 0
        min_len = float('inf')
        for right in range(n):
            win_sum+=nums[right]
            while win_sum>=target:
                min_len = min(min_len,right - left+1)
                win_sum -= nums[left]
                left+=1
            
        return 0 if min_len == float('inf') else min_len

