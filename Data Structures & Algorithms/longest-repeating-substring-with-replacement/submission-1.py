class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0

        left = 0
        
        for right in range(len(s)):
            window_size = right - left + 1
            count[s[right]] = 1 + count.get(s[right], 0)
            while window_size - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
                window_size -= 1
            ans = max(ans, window_size)
        return ans