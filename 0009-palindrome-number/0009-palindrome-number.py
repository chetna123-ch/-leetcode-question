class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans=0
        temp=x
        while  temp>0:
            r=temp%10
            ans=ans*10+r
            temp//=10
        return ans == x

        
        