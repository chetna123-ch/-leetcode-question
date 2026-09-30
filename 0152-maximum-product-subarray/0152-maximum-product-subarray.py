class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # current_product=1
        # max_product=nums[0]

        # for i in range(len(nums)):
        #     current_product*=max_product

            
        #     if current_product>max_product:
        #         max_product=current_product

        #     if current_product<0:
        #         current_product=1

        # return max_product

        # using kadanes algo
        minend = nums[0]
        maxend = nums[0]
        rest = nums[0]
        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = minend*nums[i]
            v3 = maxend*nums[i]
            maxend = max(v1,max(v2,v3))
            minend = min(v1,min(v2,v3))
            rest = max(rest,max(maxend,minend))
        return rest
