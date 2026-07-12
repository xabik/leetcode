class Solution:
    def maxArea(self, height) -> int:
        maxC = 0
        f = 0
        lx = len(height) - 1
        while f < lx:
            curC = min(height[f], height[lx]) * (lx - f)
            if curC > maxC:
                maxC = curC
            if height[f] > height[lx]:
                lx -= 1
            else:
                f += 1
        return maxC
