class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        all_odd = all(num % 2 == 1 for num in nums1)
        all_even = all(num % 2 == 0 for num in nums1)

        # Already all same parity
        if all_odd or all_even:
            return True

        # Mixed parity
        # Find the smallest element
        minimum = min(nums1)

        # If minimum is odd, all other even elements
        # can be converted to odd by subtracting minimum.
        if minimum % 2 == 1:
            return True

        # Minimum is even and array has mixed parity.
        # Minimum cannot be changed, so odd elements
        # cannot all be made even.
        return False
