class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        ans = 0
        
        for char in chars:
            count = 0
            left = 0
            for right in range(len(s)):
                window_size = right - left + 1
                if s[right] == char:
                    count += 1
                while window_size - count > k:
                    if s[left] == char:
                        count -= 1
                    left += 1
                    window_size -= 1
                ans = max(ans, window_size)
        return ans