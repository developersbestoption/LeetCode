a='@123rafi.@1'
b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
c=''
for i in a:
    if i.isalnum():
        c+=i
    else:
       continue
print(c)

