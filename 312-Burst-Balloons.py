class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        new_coins = [1] + nums + [1]
        dp = [[0] * (n+2) for i in range(n+2)]
        for l in range(n,0,-1):
            for r in range(l,n+1):
                for i in range(l,r+1):
                    max_coins = new_coins[l-1] * new_coins[i] * new_coins[r+1] + dp[l][i-1] + dp[i+1][r]
                    dp[l][r] = max(max_coins, dp[l][r])
        return dp[1][n]