class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        if len(s1) > len(s2):
            return False
        s1count = [0] * 26
        s2count = [0] * 26
        # Count first characters
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Examine right side
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            # Added a mismatch
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1

            # Examine left side
            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            #  Deleted a match
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l +=1
        return matches == 26
 
        
        