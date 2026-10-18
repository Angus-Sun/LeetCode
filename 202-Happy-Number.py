class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n,n
        while True:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False
    def sumOfSquares(self,n):
        res = 0
        while n:
            digit = n % 10
            n //= 10
            res += digit**2
        return res