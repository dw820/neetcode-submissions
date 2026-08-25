class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        def dfs(elements, i):
            if len(elements) > n:
                return
            
            output.append(elements[:])
            
            for j in range(i, n):
                num = nums[j]
                elements.append(num)
                dfs(elements, j+1)
                elements.pop()


        dfs([], 0)

        return output