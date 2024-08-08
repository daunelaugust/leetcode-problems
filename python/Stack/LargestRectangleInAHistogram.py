def largestRectangleArea(self, heights: List[int]) -> int:

    maxArea = 0
    stack = []

    for i,h in enumerate(heights):
        temp = i
        while stack and stack[-1][1] > h:
            RectI, RectH = stack.pop()
            maxArea = max(maxArea, RectH*(i-RectI))
            temp = RectI

        stack.append((temp,h))
    
    # catches the wrap around
    for i,h in stack:
        maxArea = max(maxArea, h*(len(heights)-i))



    return maxArea