class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current_sum=0
        # max_sum=nums[0]
        # for i in range(len(nums)):
        #     current_sum+=nums[i]

        #     if current_sum>max_sum:
        #         max_sum=current_sum
        #     if current_sum<0:
        #         current_sum=0

        # return max_sum

        # using kadnes algo 
        i =0
        best = nums[0]
        ans = nums[0]
        n = len(nums)
        for i in range(1,n):
            v1 = best +nums[i]
            v2 = nums[i]
            best = max(v1,v2)
            ans = max(ans,best)
        return ans
