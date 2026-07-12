class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxC = 0
        f = 0
        l = len(height) - 1
        while f < l:
            curC = min(height[f], height[l]) * (l - f)
            if curC > maxC:
                maxC = curC
            if height[f] > height[l]:
                l -= 1
            else:
                f += 1
        return maxC
