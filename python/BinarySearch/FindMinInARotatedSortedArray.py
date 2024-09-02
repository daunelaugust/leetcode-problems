def findMin(self, nums: List[int]) -> int:
    l = 0
    r = len(nums)-1

    minMid = min(nums[l],nums[r])

    while l < r:

        mid = (l+r)//2
        minMid = min(nums[mid],minMid)

        if nums[mid] > nums[l] and nums[mid]< nums[r]:
            minMid = min(nums[l],minMid)
            r = mid - 1
        elif nums[mid] > nums[l] and nums[mid] > nums[r]:
            minMid = min(nums[r],minMid)
            l = mid +1
        else:
            r = mid -1
            minMid = min(nums[r],minMid)
    return minMid   