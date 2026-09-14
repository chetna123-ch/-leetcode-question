class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l=0
        r=0    
        for i in range(n):
                if nums[r]==0:
                     r+=1
                elif nums[r]!=0:
                    temp = nums[r]
                    nums[r]= nums[l]
                    nums[l]=temp
                    r+=1
                    l+=1
            
        return None