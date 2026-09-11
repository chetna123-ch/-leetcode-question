class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        li = set()
        n= len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and j!=k and k!=i :
                        if digits[i]!=0 and digits[k]%2==0 :
                            number = digits[i] * 100 + digits[j] * 10 + digits[k]
                            li.add(number)
        
        
        return len(li)
