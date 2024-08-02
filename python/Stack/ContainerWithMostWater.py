def maxArea(self, height: List[int]) -> int:

    j = len(height) - 1
    i = 0
    maxVal=0


    while i<j:
    
        waterLine = min(height[i],height[j])
        width = j-i
        maxVal = max(waterLine*width, maxVal)
        if height[i] < height[j]:
            i+=1
        elif height[i] >= height[j]:
            j-=1
    
    return maxVal