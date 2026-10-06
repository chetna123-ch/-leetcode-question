class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        add = 0
        f = {0: 1}
        res = 0
        for i in range(len(nums)):
            add += nums[i]
            que = add - k
            if que in f:
                res += f[que]
            f[add] = f.get(add, 0) + 1
        return res
