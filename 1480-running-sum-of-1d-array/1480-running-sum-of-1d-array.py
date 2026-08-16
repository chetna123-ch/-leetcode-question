class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        add=0
        li=[]
        for i in nums:
            add+=i
            li.append(add)

        return li
