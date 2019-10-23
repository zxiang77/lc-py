class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        rmax, stk = height[0], []
        l = len(height)
        for i in range(l - 1, 0, -1):
            if not stk:
                stk.append(i)
                continue
            if height[i] >= height[stk[-1]]:
                stk.append(i)

        rain = 0
        for i in range(1, l - 1):
            v = height[i]
            if stk[-1] == i:
                stk.pop()
            rain += max(0, min(rmax, height[stk[-1]]) - v)
            rmax = max(rmax, v)
        return rain