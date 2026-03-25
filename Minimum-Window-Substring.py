1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if t == "":
4            return ""
5        
6        window, t_map = {}, {}
7        
8        for c in t:
9            t_map[c] = 1 + t_map.get(c, 0)
10        
11        l = 0
12        res, resLen = [-1, -1], float("infinity")
13        have, need = 0, len(t_map)
14        for r in range(len(s)):
15            window[s[r]] = 1 + window.get(s[r], 0)
16            if s[r] in t_map and window[s[r]] == t_map[s[r]]:
17                have += 1
18            while have == need:
19                if (r - l + 1) < resLen:
20                    res = [l, r]
21                    resLen = r - l + 1
22                window[s[l]] -= 1
23                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
24                    have -= 1
25                l += 1
26        l, r = res
27        return s[l:r+1] if resLen != float("infinity") else ""