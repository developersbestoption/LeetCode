class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        new_num=0
        sto=x
        while True:
            last_num=x%10
            if x==0:
                break
            new_num=new_num*10+last_num
            x//=10
        return new_num==sto
a=Solution()
print(a.isPalindrome(234))
