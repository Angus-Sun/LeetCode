class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_map = [0] * 26
        s2_map = [0] * 26

        for i in range(len(s1)):
            s1_map[ord(s1[i])-ord('a')] += 1
            s2_map[ord(s2[i])-ord('a')] += 1
        have = 0
        need = 26

        for i in range(len(s1_map)):
            if s1_map[i] == s2_map[i]:
                have += 1
        if have == need:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            c = ord(s2[r])-ord('a')
            if s1_map[c]== s2_map[c]+1:
                have += 1
            elif s1_map[c] == s2_map[c]:
                have -= 1
            s2_map[c] += 1
            c= ord(s2[l]) - ord('a')
            if s1_map[c] == s2_map[c]-1:
                have += 1
            elif s1_map[c] == s2_map[c]:
                have -= 1
            s2_map[c] -= 1
            l += 1
            if have == need:
                return True
        return have == need
            