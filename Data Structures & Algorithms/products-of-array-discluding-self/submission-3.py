class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        c = 0
        n = len(nums)
        for i in nums:
            if i==0:
                c+=1
            else:
                p*=i
        
        z = []
        for i in nums:
            if c>0 and c==1:
                if i==0:
                    z.append(p)
                else:
                    z.append(0)
            elif c==0:
                z.append(int(p/i))
            else:
                z.append(0)
        return z