class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
inp=list(map(int,input("enter the linked list values ").split()))
head=Node(inp[0])
current=head
for i in range(1,len(inp)):
    current.next=Node(inp[i])
    current=current.next
current=head
while current:
    print(current.data)
    current=current.next
'''
a=Node(44)
b=Node(55)
c=Node(66)
a.next=b
b.next=c
current=a
while current:
    print(current.data)
    current=current.next
    '''
'''    
print(a.data)
print(b.next.data) 
print(a.next.data)
   ''' 
    
    