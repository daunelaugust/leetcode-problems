def trap(height):
    tempSum = 0
    realSum = 0
    n = len(height)
    
    if n == 0:
        return 0

    i, j = 0, 1
    
    while i < n - 1:
        if j == n:
            i += 1
            j = i + 1
            tempSum = 0
            continue

        if i == 0 and height[i] == 0:
            i += 1
            j = i + 1
            continue

        if height[j] < height[i]:
            tempSum += (height[i] - height[j])
            j += 1
        else:
            realSum += tempSum
            tempSum = 0
            i = j
            j = i + 1

    return realSum

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
