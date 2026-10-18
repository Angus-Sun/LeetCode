class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n,n
        while True:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            if slow == fast:
                break
        return fast == 1
    def sumOfSquares(self,n):
        res = 0
        while n:
            digit = n % 10
            n //= 10
            res += digit**2
        return res