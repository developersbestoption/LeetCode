class Solution:
    def reverse(self, x: int) -> int:
        while x%10==0 and x!=0:
            x//=10
        print(x)
        new_num=0
        num_2=x
        if x<0:
            x=-x
        while x:
            ls=x%10
            x//=10
            if ls==0 and ls!=0:
                continue
            new_num+=ls
            if x==0:
                break
            new_num*=10
        if -2**31 <=new_num<= 2**31 - 1:
            if num_2<0:
                return(-new_num)
            else:
                return(new_num)
        else:
            return 0
a=Solution()
print(a.reverse(1534236469))

