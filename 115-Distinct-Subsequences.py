class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        dp = [1] * (len(s)+1)
        for i in range(len(t)-1,-1,-1):
            nextDP = [0] *(len(s)+1)
            for j in range(len(s)-1,-1,-1):
                nextDP[j] = nextDP[j+1]
                if t[i] == s[j]:
                    nextDP[j] += dp[j+1]
            dp = nextDP
        return dp[0]

