class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1map, s2map = {}, {}
        for c in s1:
            s1map[c] = 1+ s1map.get(c, 0)
        l, r = 0, len(s1)-1
        for i in range(r):
            s2map[s2[i]] = 1 + s2map.get(s2[i], 0)
        for i in range(r, len(s2)):
            s2map[s2[i]] = 1 + s2map.get(s2[i], 0)
            if s2map == s1map:
                return True
            s2map[s2[l]] -= 1
            if s2map[s2[l]] == 0:
                del s2map[s2[l]]
            l += 1
        return False