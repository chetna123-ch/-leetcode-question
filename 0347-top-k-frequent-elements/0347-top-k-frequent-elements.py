from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # Sort by frequency descending
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in sorted_items[:k]]
        