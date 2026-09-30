class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        max_freq = 0
        char_counts = {}

        for right in range(len(s)):
            # Update the count of the current character
            ch = s[right]
            char_counts[ch] = char_counts.get(ch, 0) + 1
            
            # Track the maximum frequency of a single character seen in the current window
            max_freq = max(max_freq, char_counts[ch])
            
            # Current window size is (right - left + 1)
            # If the number of characters to replace exceeds k, shrink the window from the left
            if (right - left + 1) - max_freq > k:
                char_counts[s[left]] -= 1
                left += 1
                
            # The window size is guaranteed to be valid or valid-maximal at this point
            max_len = max(max_len, right - left + 1)
            
        return max_len
