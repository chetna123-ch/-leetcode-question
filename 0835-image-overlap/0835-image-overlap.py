class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        for row_shift in range(-(n - 1), n):
            for col_shift in range(-(n - 1), n):

                count = 0

                for row in range(n):
                    for col in range(n):

                        row2 = row + row_shift
                        col2 = col + col_shift

                        if 0 <= row2 < n and 0 <= col2 < n:
                            if img1[row][col] == 1 and img2[row2][col2] == 1:
                                count += 1

                max_overlap = max(max_overlap, count)

        return max_overlap