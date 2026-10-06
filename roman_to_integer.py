"""class Solution:
    def romanToInt(self, s: str) -> int:
        """
'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
'''
values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
a="IIIVMIIIXX"
num=0
for i in range(len(a)):
    if i+1<len(a) and values[a[i]] < values[a[i+1]]:
        num=num-values[a[i]]
    else:
        num+=values[a[i]]
print(num)