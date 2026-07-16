class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r
        while l <= r:
            m = l + (r-l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)
            if hours <= h:
                min_k = m
                r = m-1
            else:
                l = m+1
        return min_k