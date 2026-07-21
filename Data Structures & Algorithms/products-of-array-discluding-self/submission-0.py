class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] 
        suf = [1] 

        for i in range(n-1):
            pre.append(nums[i]*pre[-1])

        for j in range(n-1, 0, -1):
            suf.append(nums[j]*suf[-1])
        
        suf.reverse()

        out = []

        for k in range(n):
            out.append(pre[k] * suf[k])

        return out