class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies=max(candies)
        ls=[]
        for i in candies:
            if i+extraCandies>=maxCandies:
                ls.append(True)
            else:
                ls.append(False)
        return ls
        