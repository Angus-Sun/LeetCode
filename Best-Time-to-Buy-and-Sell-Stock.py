1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        l, r = 0, 1
4        maxProfit = 0
5        while r < len(prices):
6            if prices[r] > prices[l]:
7                profit = prices[r] - prices[l]
8                maxProfit = max(profit, maxProfit)
9            else:
10                l = r
11            r += 1
12        return maxProfit