class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        #flag=True
        for i in range(len(nums)):
            sum=0
            if nums[i]>=0 and nums[i]<=9:
                if i==nums[i]:
                    return i
                else :
                    flag=False
            else:
                old=nums[i]
                while old:
                    l=old%10
                    sum+=l
                    old//=10
                if i==sum:
                    return i
                else :
                    flag=False
        if not flag:
            return -1 
a=Solution()
print(a.smallestIndex([619,916,21,4,4,835]))
