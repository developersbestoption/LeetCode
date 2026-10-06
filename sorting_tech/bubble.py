a=[0,1,99,3,6,5,33,00,0]
for i in range(len(a)):
    for j in range(len(a)):
        if j+1<len(a) and a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)