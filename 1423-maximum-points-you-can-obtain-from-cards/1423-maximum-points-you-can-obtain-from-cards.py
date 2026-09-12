class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        rsum = 0
        maxsum = 0
        rindex = len(cardPoints) - 1

        # Initially take k cards from left
        for i in range(k):
            lsum += cardPoints[i]

        maxsum = lsum

        # One-by-one left card remove, right card add
        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rindex]
            rindex -= 1

            maxsum = max(maxsum, lsum + rsum)

        return maxsum