class Solution:
    @staticmethod
    def fun(n: int) -> int:
        sum_ = 0
        while n > 0:
            d = n % 10
            sum_ += d * d
            n //= 10  # Use integer division
        return sum_

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.fun(n)
        
        # Move slow by 1 step and fast by 2 steps
        while slow != fast:
            slow = self.fun(slow)
            fast = self.fun(self.fun(fast))
            
        return slow == 1
