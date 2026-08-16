class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        z = []
        n = len(nums) 
        for i in range(n):
            l = i+1
            r = n-1       
            while l<r:
                if nums[l]+nums[r]+nums[i]==0 and [nums[i],nums[l],nums[r]] not in z:
                    z.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif (nums[l]+nums[r])+nums[i]>0:
                    r-=1
                else:
                    l+=1
        return z