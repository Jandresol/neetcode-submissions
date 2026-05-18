class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        window = [0] * 52
        tCount = [0] * 52

        res = [0,0]
        resLen = float('inf')
        l = 0

        def char_to_index(c):
            if 'A' <= c <= 'Z':
                return ord(c) - ord('A')
            return ord(c) - ord('a') + 26

        # Counting t characters
        for char in t:
            tCount[char_to_index(char)] += 1

        have = 0
        need = 0
        for count in tCount:
            if count > 0:
                need +=1

        for r in range(len(s)):
            ri = char_to_index(s[r])
            li = char_to_index(s[l])
            window[ri] += 1

            if tCount[ri] == window[ri]:
                have += 1

            # Met condition
            while need == have:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                li = char_to_index(s[l])
                window[li] -= 1
                if tCount[li] > 0 and window[li] < tCount[li]:
                    have -= 1
                l += 1
        l, r = res
        if resLen == float('inf'):
            return ""
        return s[l : r +1]

    


        
        