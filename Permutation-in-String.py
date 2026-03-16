1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        if len(s1) > len(s2):
4            return False
5        s1map, s2map = {}, {}
6        for c in s1:
7            s1map[c] = 1+ s1map.get(c, 0)
8        l, r = 0, len(s1)-1
9        for i in range(r):
10            s2map[s2[i]] = 1 + s2map.get(s2[i], 0)
11        for i in range(r, len(s2)):
12            s2map[s2[i]] = 1 + s2map.get(s2[i], 0)
13            if s2map == s1map:
14                return True
15            s2map[s2[l]] -= 1
16            if s2map[s2[l]] == 0:
17                del s2map[s2[l]]
18            l += 1
19        return False