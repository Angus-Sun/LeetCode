class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        window, t_map = {}, {}

        for i in range(len(t)):
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        
        have, need = 0, len(t_map)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in t_map and window[c] == t_map[c]:
                have += 1
            
            while have == need:
                if r-l+1 < resLen:
                    res, resLen = [l, r], r-l+1
                c = s[l]
                window[c] -= 1
                if c in t_map and window[c] < t_map[c]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen < float("infinity") else ""
                