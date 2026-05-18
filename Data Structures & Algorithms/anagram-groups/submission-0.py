class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # The array is the key, make it tuple so it is immutable
            groups[tuple(count)].append(s)
            
        return list(groups.values())
                

        