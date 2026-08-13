class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        s_map, t_map = {}, {}
        res, resLen = [-1,-1], float("infinity")
        for i in range(len(t)):
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        have, need = 0, len(t_map)
        l = 0
        for r in range(len(s)):
            if s[r] in t_map and s_map.get(s[r], 0) + 1 == t_map[s[r]]:
                have += 1
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r-l+1
                if s[l] in t_map and s_map.get(s[l], 0) == t_map[s[l]]:
                    have -= 1
                s_map[s[l]] -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
            

