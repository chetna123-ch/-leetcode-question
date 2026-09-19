class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr_alt =0
        max_alt =0
        n = len(gain)
        for i in range(n):
            curr_alt +=gain[i]
            max_alt = max(max_alt,curr_alt)
        return max_alt