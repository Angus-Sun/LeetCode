class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = {} # (buying, i) : val
        def dfs(buying, i):
            if i >= len(prices):
                return 0
            if (buying, i) in dp:
                return dp[(buying, i)]
            cooldown = dfs(buying, i+1)
            if buying:
                buy = dfs(not buying, i+1) - prices[i]
                dp[(buying, i)] = max(buy, cooldown)
            else:
                sell = dfs(not buying, i+2) + prices[i]
                dp[(buying, i)] = max(sell, cooldown)
            return dp[(buying, i)]
        return dfs(True, 0)
        
        