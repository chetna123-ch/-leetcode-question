class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = {}

        for num in arr:
            dict1[num] = dict1.get(num, 0) + 1

        freq_values = list(dict1.values())

        return len(freq_values) == len(set(freq_values))

