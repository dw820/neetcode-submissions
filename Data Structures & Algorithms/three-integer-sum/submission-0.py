class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = set()

        for i in range(len(nums)-2):
            target = -nums[i]

            l = i+1
            r = len(nums) - 1

            while l < r:
                cur = nums[l] + nums[r]
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        
        return [list(x) for x in ans]
