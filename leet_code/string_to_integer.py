class Solution:
    def conv(self,str):
        a=0
        count=0
        for i in str:
            if i=='-' or i=='+':
                count+=1
                continue
            c=ord(i)-ord('0')
            a+=c
            count+=1
            if count<len(str):
                a*=10
        if str[0]=='-':
             a-=(a+a)
        if a<-2147483648:
            return -2147483648
        elif a>2147483647:
            return 2147483647
        else:
            return a
    def myAtoi(self, s: str) -> int:
        b=""
        c=s.strip()
        for i in c:
            if (i=='-' or i=='+') and len(b)==0:
                b+=i
            elif i.isalpha() or i.isspace():
                break
            elif i.isdigit():
                b+=i
            else:
                break
        if len(b)>=1:
            if b[0]=='-' or b[0]=='+':
               if len(b)>1:
                   return self.conv(b)
               else:
                   return 0
            else:
                return self.conv(b)
        else:
            return 0
a=Solution()
print(a.myAtoi("+1"))
'''
-
'''