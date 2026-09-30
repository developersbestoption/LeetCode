class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a=int(''.join(map(str,digits)))
        a+=1
        #ls=list(int(map(str,a).split()))
        new_ls=[]
        while a:
            new_ls.append(a%10)
            a//=10
        new_ls.reverse()
        return new_ls
abc=Solution()
print(abc.plusOne([9]))
