class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Looking for pound
            while s[j] != '#':
                j += 1
            # Length = the number before the pound
            length = int(s[i:j])
            start_char = j + 1
            end_char = start_char + length
            res.append(s[start_char:end_char])
            i = end_char

        return res
