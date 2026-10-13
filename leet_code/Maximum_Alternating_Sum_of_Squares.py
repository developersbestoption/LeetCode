class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        #----sorting-----
# u can use below line for sorting the array to save the time for large number inouts
        #nums.sort(key=abs, reverse=True)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j+1 <len(nums) and abs(nums[j])<abs(nums[j+1]):
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
        #---------creating optimal list--------------
        if len(nums)%2==0:
            r=len(nums)//2
        else:
            r=(len(nums)//2)+1
        optimal=[]
        for i in range(r):
            optimal.append(nums[i])
            if i==(len(nums)//2) and len(nums)%2!=0:
                break
            optimal.append(nums[-i-1])
        #-------adding the values--------
        def sum(self,a):
            sum=0
            for i in range(len(a)):
                    if i==0 or i%2==0:
                        sum+=a[i]**2
                    else:
                        sum-=a[i]**2
            return sum
        return sum(self,optimal)
a=Solution()
print(a.maxAlternatingSum([1, 2, 3, 4, 5]))

