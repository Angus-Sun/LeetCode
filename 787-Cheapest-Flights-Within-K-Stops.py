class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        while k >= 0:
            temp = prices.copy()
            for source, destination, price in flights:
                if prices[source] + price < temp[destination]:
                    temp[destination] = prices[source] + price
            prices = temp
            k -= 1
        return prices[dst] if prices[dst] != float("infinity") else -1