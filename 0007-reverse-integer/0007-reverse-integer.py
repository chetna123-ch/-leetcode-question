class Solution:
    def reverse(self, x: int) -> int:
            sign = -1 if x < 0 else 1
            x = abs(x)
    
            reversed_num = 0
            while x > 0:
                reversed_num = (reversed_num * 10) + (x % 10)
                x //= 10
        
            reversed_num *= sign
    
            if reversed_num < -2147483648 or reversed_num > 2147483647:
                return 0
        
            return reversed_num
