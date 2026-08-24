class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area = float('-inf')

        while l < r:
            h_l = heights[l]
            h_r = heights[r]
            h = min(h_l, h_r)
            w = r - l
            area = h * w
            max_area = max(max_area, area)

            if h_l < h_r:
                l += 1
            elif h_l > h_r:
                r -= 1
            else:
                l += 1
                r -= 1

        return max_area