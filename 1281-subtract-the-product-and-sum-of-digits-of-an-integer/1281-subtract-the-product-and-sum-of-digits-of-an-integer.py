class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        s=0
        tmp = n
        while tmp>0:
            r=tmp%10
            s+=r
            p*=r
            tmp//=10
        return p-s

        